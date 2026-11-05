"""SDK smoke run on a dedicated Mozi instance: python -m examples.mozi_rl_quickstart scenario.xml"""

import argparse

from mozi_rl import make_env


def main():
    parser = argparse.ArgumentParser(description="Run one Mozi RL episode with a no-op policy")
    parser.add_argument("scenario", help="Name of a scenario accepted by LoadScenario")
    parser.add_argument("--side", default="蓝", help="Unique side name or substring")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--rest-port", type=int, default=8082)
    parser.add_argument("--ws-port", type=int, default=8050)
    parser.add_argument("--steps", type=int, default=3)
    parser.add_argument("--frames-per-step", type=int, default=1)
    parser.add_argument("--record", default="run_data/mozi_rl_smoke.jsonl")
    args = parser.parse_args()

    env = make_env(args.scenario, side_name=args.side, host=args.host,
                   rest_port=args.rest_port, ws_port=args.ws_port,
                   max_steps=args.steps, frames_per_step=args.frames_per_step,
                   trajectory_path=args.record)
    try:
        obs, info = env.reset()
        print(f"reset: {obs['scenario_name']}, units={len(obs['units'])}, contacts={len(obs['contacts'])}")
        while True:
            obs, reward, terminated, truncated, info = env.step(None)
            print(f"step={info['step']} game_delta={info['sim_delta_sec']:.1f}s "
                  f"units={len(obs['units'])} contacts={len(obs['contacts'])} reward={reward}")
            if terminated or truncated:
                break
    finally:
        env.close()


if __name__ == "__main__":
    main()
