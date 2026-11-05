"""JSONL trajectory export for later training and offline evaluation."""

import json
from pathlib import Path


class TrajectoryRecorder:
    def __init__(self, env, path: str | Path):
        self.env = env
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._file = self.path.open("a", encoding="utf-8")
        self._episode = 0
        self._previous = None

    def _write(self, event: dict):
        self._file.write(json.dumps(event, ensure_ascii=False, allow_nan=False) + "\n")
        self._file.flush()

    def reset(self, **kwargs):
        observation, info = self.env.reset(**kwargs)
        self._episode += 1
        self._previous = observation
        self._write({"kind": "reset", "episode": self._episode,
                     "observation": observation, "info": info})
        return observation, info

    def step(self, action):
        observation, reward, terminated, truncated, info = self.env.step(action)
        self._write({"kind": "transition", "episode": self._episode,
                     "observation": self._previous, "action": action,
                     "next_observation": observation, "reward": reward,
                     "terminated": terminated, "truncated": truncated, "info": info})
        self._previous = observation
        return observation, reward, terminated, truncated, info

    def close(self):
        self._file.close()
        self.env.close()
