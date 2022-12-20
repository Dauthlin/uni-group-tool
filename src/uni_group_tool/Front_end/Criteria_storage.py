class CriteriaStorage:
    def __init__(self):
        self.diversity = {"gender": False, "home": False, "average": False}
        self.amount_to_be_together = {"Gender": {"Male": None, "Female": None}, "home": {"Home": None, "Online": None}}
        self.specific_teams= []

    def get_all(self):
        return self.__dict__

    def set_all(self, dict1):
        self.__dict__ = dict1

    def get_diversity(self, key) -> int | None:
        return self.diversity[key]

    def set_diversity(self, key: str):
        self.diversity[key] = not self.diversity[key]     # type: ignore

    def get_should_be_together(self, outer_key: str, inner_key: str) -> int | None:
        return self.amount_to_be_together[outer_key][inner_key]

    def set_should_be_together(self, outer_key: str, inner_key: str, value: int):
        self.amount_to_be_together[outer_key][inner_key] = value    # type: ignore

    def set_specific_teams(self, value: list):
        self.specific_teams = value     # type: ignore
