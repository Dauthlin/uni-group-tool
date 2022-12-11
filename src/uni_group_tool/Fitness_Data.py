class FitnessData:
    def __init__(self):
        self.diversity = {"gender": None, "home": None, "average": None}
        self.should_be_together = {"gender": {"M": None, "F": None}, "home": {"H": None, "O": None}}
        self.has_required_students = None


    def get_all(self):
        return self.__dict__

    def set_all(self,dict1):
        self.__dict__ = dict1


    def get_diversity(self, key) -> dict:
        return self.diversity[key]

    def set_diversity(self, key: str, value: int):
        self.diversity[key] = value

    def get_should_be_together(self, outer_key: str, inner_key: str) -> dict:
        return self.should_be_together[outer_key][inner_key]

    def set_should_be_together(self, outer_key: str, inner_key: str, value: int):
        self.should_be_together[outer_key][inner_key] = value

    def get_has_required_students(self) -> dict:
        return self.has_required_students

    def set_has_required_students(self, value: int):
        self.has_required_students = value
