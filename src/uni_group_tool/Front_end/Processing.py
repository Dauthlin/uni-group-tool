import customtkinter
from uni_group_tool.main import run


class processing:
    def __init__(self, all_data):
        self.all_data = all_data
        for i in run(
            self.all_data.criteria,
            int(self.all_data.size_of_teams),
            self.all_data.shuffle,
            self.all_data.weights,
            self.all_data.data_path,
            self.all_data.debugging,
            self.all_data.saving,
        ):
            print(i)
