"""Contract tests for the research environment; no tactical policy or live server."""

import unittest
from contextlib import contextmanager
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import Mock

from requests import Response

from src.rl_env import EnvironmentConfig, MoziBackend, MoziRLEnv, validate_actions
from src.rl_env.mozi_backend import CommandRejected
from src.rl_env.recording import TrajectoryRecorder
from src.mozi_api.connector import MoziConnector
import mozi_rl


def observation(t=0):
    return {"sim_time_sec": t, "frame_seq": t // 11, "units": [{"id": "blue-1"}],
            "contacts": [{"id": "contact-1"}], "scenario_name": "example"}


class Backend:
    def __init__(self):
        self.time = 0
        self.commands = []

    def reset(self, scenario_name):
        self.time = 0
        return observation()

    def apply_actions(self, actions):
        self.commands.extend(actions)
        return [{"action": x, "accepted": True} for x in actions]

    def advance(self, frames):
        self.time += frames * 11
        return observation(self.time)

    def close(self):
        pass


class EnvTests(unittest.TestCase):
    def test_step_uses_real_game_delta_and_truncates(self):
        backend = Backend()
        env = MoziRLEnv(backend, EnvironmentConfig("example", frames_per_step=1,
                                                    episode_duration_sec=20),
                        reward_fn=lambda old, actions, new, info: (info["sim_delta_sec"], {}))
        initial, info = env.reset(seed=42)
        self.assertEqual(initial["sim_time_sec"], 0)
        self.assertFalse(info["seed_applied"])
        _, reward, terminal, truncated, info = env.step({"type": "speed", "unit_id": "blue-1", "speed_kmh": 600})
        self.assertEqual(reward, 11)
        self.assertEqual(info["sim_delta_sec"], 11)
        self.assertFalse(terminal or truncated)
        _, _, terminal, truncated, _ = env.step(None)
        self.assertFalse(terminal)
        self.assertTrue(truncated)
        with self.assertRaises(RuntimeError):
            env.step(None)

    def test_invalid_batch_never_reaches_backend(self):
        backend = Backend()
        env = MoziRLEnv(backend, EnvironmentConfig("example"))
        env.reset()
        with self.assertRaisesRegex(ValueError, "不属于当前己方"):
            env.step([{"type": "takeoff", "unit_id": "blue-1"},
                      {"type": "takeoff", "unit_id": "red-1"}])
        self.assertEqual(backend.commands, [])
        with self.assertRaisesRegex(ValueError, "当前己方已探测"):
            validate_actions({"type": "weapon_assignment", "unit_id": "blue-1",
                              "weapon_dbid": 5, "target_id": "hidden-red"}, observation())

    def test_terminal_callback(self):
        env = MoziRLEnv(Backend(), EnvironmentConfig("example", frames_per_step=1),
                        terminal_fn=lambda current, info: current["sim_time_sec"] >= 31)
        env.reset()
        _, _, terminal, truncated, _ = env.step(None)
        self.assertFalse(terminal or truncated)
        env.step(None)
        _, _, terminal, truncated, _ = env.step(None)
        self.assertTrue(terminal)
        self.assertFalse(truncated)

    def test_recorded_transition_contains_actual_elapsed_time(self):
        temp_root = Path(__file__).resolve().parents[1] / "tmp"
        temp_root.mkdir(exist_ok=True)
        with TemporaryDirectory(dir=temp_root) as folder:
            recorder = TrajectoryRecorder(
                MoziRLEnv(Backend(), EnvironmentConfig("example", frames_per_step=1)),
                Path(folder) / "trajectory.jsonl")
            recorder.reset()
            recorder.step(None)
            recorder.close()
            records = [json.loads(line) for line in (Path(folder) / "trajectory.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual([row["kind"] for row in records], ["reset", "transition"])
        self.assertEqual(records[1]["info"]["sim_delta_sec"], 11)

    def test_public_sdk_factory_exposes_environment(self):
        env = mozi_rl.make_env("sample.xml", side_name="蓝", max_steps=3)
        try:
            self.assertIsInstance(env, MoziRLEnv)
            self.assertEqual(env.config.max_steps, 3)
        finally:
            env.close()


class FakeConnector:
    def __init__(self):
        self.data = {"ScenarioName": "example", "side": [
            {"id": "blue-side", "name": "蓝方", "activeUnits": [
                {"id": "blue-1", "name": "Blue", "UnitType": "Aircraft", "Latitude": 30, "Longitude": 80}],
             "contacts": [{"id": "seen-red", "name": "Red contact", "UnitType": "Aircraft"}]},
            {"id": "red-side", "name": "红方", "activeUnits": [
                {"id": "secret-red", "name": "Hidden red", "UnitType": "Aircraft"}], "contacts": []}],
            "FightTree": [{"SideID": "blue-side", "FightTree": [
                {"id": "parked-1", "name": "Parked", "UnitType": "Aircraft", "AirCraftInFacility": True}]}]}
        self.calls = []

    @contextmanager
    def consistent_read(self):
        yield {"sequence": 7}

    def get_full_state(self): return self.data
    def get_scenario_elapsed_seconds(self): return 0
    def set_course(self, guid, points):
        self.calls.append((guid, points))
        return True
    def set_speed(self, guid, speed): return False
    def set_weapon_control(self, guid, mode, air_mode):
        self.calls.append(("weapon_control", guid, mode, air_mode))
        return {"code": 0}
    def get_weapon_status(self, guid):
        return {"weapon_list": [{"name": "game weapon", "count": 1}]}


class ResetConnector(FakeConnector):
    def __init__(self):
        super().__init__()
        self.data["ScenarioName"] = "old"
        self.sequence = 7
        self.elapsed = 90
        self.loaded = False
        self.started = False
        self.pauses = 0

    def is_connected(self): return True
    @contextmanager
    def consistent_read(self):
        yield {"sequence": self.sequence}
    def pause_simulation(self):
        self.pauses += 1
        return {"code": 0}
    def start_simulation(self):
        self.started = True
        return {"code": 0}
    def get_update_sequence(self): return self.sequence
    def load_scenario(self, name):
        self.loaded = True
        self.sequence = 8
        self.data["ScenarioName"] = "example"
        self.elapsed = 0
        return {"code": 0, "data": {"scenarioName": "example"}}
    def wait_for_new_update(self, previous, timeout):
        if self.started and self.sequence <= previous:
            self.sequence += 1
            self.elapsed += 11
        return self.sequence if self.sequence > previous else None
    def get_scenario_name(self): return self.data["ScenarioName"]
    def get_scenario_elapsed_seconds(self): return self.elapsed


class MoziBackendTests(unittest.TestCase):
    def test_reset_waits_for_loaded_scenario_and_fresh_time(self):
        connector = ResetConnector()
        obs = MoziBackend(connector, side_name="蓝").reset("example.xml")
        self.assertTrue(connector.loaded)
        self.assertEqual(obs["scenario_name"], "example")
        self.assertEqual(obs["frame_seq"], 8)
        self.assertEqual(obs["sim_time_sec"], 0)
        self.assertTrue(connector.started)
        self.assertEqual(connector.pauses, 0)

    def test_step_waits_for_stream_frame_without_pausing(self):
        connector = ResetConnector()
        backend = MoziBackend(connector, side_name="蓝")
        env = MoziRLEnv(backend, EnvironmentConfig("example.xml", frames_per_step=1))
        env.reset()
        obs, _, _, _, info = env.step(None)
        self.assertEqual(obs["frame_seq"], 9)
        self.assertEqual(info["sim_delta_sec"], 11)
        self.assertEqual(connector.pauses, 0)

    def test_observation_is_selected_side_only(self):
        backend = MoziBackend(FakeConnector(), side_name="蓝方")
        obs = backend.observe()
        self.assertEqual({u["id"] for u in obs["units"]}, {"blue-1", "parked-1"})
        self.assertEqual([c["id"] for c in obs["contacts"]], ["seen-red"])
        self.assertNotIn("secret-red", str(obs))

    def test_optional_weapon_inventory_is_observed(self):
        obs = MoziBackend(FakeConnector(), side_name="蓝", include_weapon_status=True).observe()
        self.assertEqual(obs["weapon_status_by_unit"]["blue-1"]["weapon_list"][0]["count"], 1)
        self.assertNotIn("secret-red", obs["weapon_status_by_unit"])

    def test_heading_and_weapon_mode_decode_to_native_api(self):
        connector = FakeConnector()
        backend = MoziBackend(connector, side_name="蓝")
        obs = backend.observe()
        actions = validate_actions([
            {"type": "heading", "unit_id": "blue-1", "heading_deg": 90, "distance_km": 50},
            {"type": "weapon_control", "unit_id": "blue-1", "air_mode": "Free"},
        ], obs)
        backend.apply_actions(actions)
        self.assertGreater(connector.calls[0][1][0]["lon"], 80)
        self.assertEqual(connector.calls[1], ("weapon_control", "blue-1", "Hold", "Free"))

    def test_partial_command_failure_is_explicit(self):
        backend = MoziBackend(FakeConnector(), side_name="蓝方")
        with self.assertRaises(CommandRejected) as raised:
            backend.apply_actions([{"type": "course", "unit_id": "blue-1",
                                    "waypoints": [{"lat": 29, "lon": 81}]},
                                   {"type": "speed", "unit_id": "blue-1", "speed_kmh": 500}])
        self.assertEqual(len(raised.exception.completed), 2)
        self.assertTrue(raised.exception.completed[0]["accepted"])
        self.assertFalse(raised.exception.completed[1]["accepted"])

    def test_load_scenario_response_failure_is_not_silent(self):
        connector = MoziConnector()
        session = Mock()
        response = Response()
        response.status_code = 200
        response.headers["Content-Type"] = "application/json"
        response._content = b'{"code": 9, "message": "scenario missing"}'
        import threading
        connector._sessions[threading.get_ident()] = session
        session.request.return_value = response
        try:
            with self.assertRaisesRegex(RuntimeError, "scenario missing"):
                connector.load_scenario("missing.xml")
        finally:
            connector.close()


if __name__ == "__main__":
    unittest.main()
