from models.stages import get_default_stages


class HybridSystem:
    def __init__(self):
        self.stages = get_default_stages()

    def get_stage(self, t):
        if t < 0.006:
            return self.stages[0]
        if t < 0.014:
            return self.stages[1]
        return self.stages[2]
