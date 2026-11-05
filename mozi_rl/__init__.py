"""Public SDK entry point for Mozi reinforcement learning experiments."""

from pathlib import Path

from src.mozi_api.connector import MoziConnector as _MoziConnector
from src.rl_env import (AttritionDiscoveryReward, EnvironmentConfig, MoziBackend,
                        MoziRLEnv, TrajectoryRecorder, ZeroReward, validate_actions)
from src.rl_env.mozi_backend import CommandRejected

__version__ = "0.1.0"


def make_env(scenario_name: str, *, side_name: str = "蓝", host: str = "127.0.0.1",
             rest_port: int = 8082, ws_port: int = 8050,
             frames_per_step: int = 1, episode_duration_sec: float = 3600.0,
             max_steps: int | None = None, reward_fn=None, terminal_fn=None,
             trajectory_path: str | Path | None = None,
             include_weapon_status: bool = False):
    """Create one exclusive live environment; calling reset loads the scenario."""
    connector = _MoziConnector(host=host, rest_port=rest_port, ws_port=ws_port)
    env = MoziRLEnv(
        MoziBackend(connector, side_name=side_name, include_weapon_status=include_weapon_status),
        EnvironmentConfig(scenario_name, frames_per_step,
                          episode_duration_sec, max_steps),
        reward_fn=reward_fn, terminal_fn=terminal_fn,
    )
    return TrajectoryRecorder(env, trajectory_path) if trajectory_path is not None else env


__all__ = ["__version__", "make_env", "MoziBackend", "MoziRLEnv",
           "EnvironmentConfig", "TrajectoryRecorder", "ZeroReward",
           "AttritionDiscoveryReward", "CommandRejected", "validate_actions"]
