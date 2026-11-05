"""Reward plugins. Scores are derived only from observations available to the policy."""


class ZeroReward:
    def __call__(self, previous: dict, actions: list[dict], current: dict, info: dict):
        return 0.0, {}


class AttritionDiscoveryReward:
    """Optional example shaping; not a universal win/loss score."""

    def __init__(self, own_loss_penalty: float = 1.0, discovery_reward: float = 0.1,
                 time_penalty_per_sec: float = 0.0):
        self.own_loss_penalty = float(own_loss_penalty)
        self.discovery_reward = float(discovery_reward)
        self.time_penalty_per_sec = float(time_penalty_per_sec)

    def __call__(self, previous: dict, actions: list[dict], current: dict, info: dict):
        old_units = {u["id"] for u in previous["units"]}
        new_units = {u["id"] for u in current["units"]}
        old_contacts = {c["id"] for c in previous["contacts"]}
        new_contacts = {c["id"] for c in current["contacts"]}
        components = {
            "own_units_disappeared": -self.own_loss_penalty * len(old_units - new_units),
            "new_contacts": self.discovery_reward * len(new_contacts - old_contacts),
            "time": -self.time_penalty_per_sec * info["sim_delta_sec"],
        }
        return sum(components.values()), components
