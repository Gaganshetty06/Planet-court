class PlanetCourtEnv:
    def __init__(self):
        self.step_count = 0

    def state(self):
        return {"step": self.step_count}