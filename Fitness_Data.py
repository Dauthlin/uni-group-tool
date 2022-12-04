class FitnessData:
    def __init__(self):
        self.diversity = {"gender": None, "home": None, "average": None}

    def get_diversity(self, key) -> dict:
        return self.diversity[key]

    def set_diversity(self, key: str, value: int):
        self.diversity[key] = value
