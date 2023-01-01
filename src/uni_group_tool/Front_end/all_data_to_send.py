from .Criteria_storage import CriteriaStorage
class AllDataToSend:
    def __init__(self):
        self.size_of_teams = 2
        self.shuffle = True
        self.criteria = None
        self.weights = {}
        self.data_path = None
        self.debugging = False
        self.saving = False
        self.min_group_size_or_amount_of_groups = True
        self.result_path = None

    def get_all(self):
        return self.__dict__

    def set_all(self, dict1):
        self.__dict__ = dict1
    def set_result_path(self, path):
        self.result_path = path

    def get_result_path(self):
        return self.result_path
    def set_size_of_teams(self, value):
        self.size_of_teams = int(value)
    def shuffle(self, value: bool):
        self.size_of_teams = value
    def set_min_group_size_or_amount_of_groups(self, value: bool):
        self.min_group_size_or_amount_of_groups = value
    def set_criteria(self, value: CriteriaStorage):
        self.criteria = value

    def set_weights(self, key,value):
        self.weights[key] = value

    def set_data_path(self, value: str):
        self.data_path = value

    def set_debugging(self, value: bool):
        self.debugging = value

    def set_saving(self, value: bool):
        self.saving = value