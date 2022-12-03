class groups:
    def __init__(self,All):
        self.groups = All

    def get_groups(self):
        return self.groups

    def add_group(self, group):
        self.groups.append(group)

    def number_of_groups(self):
        return len(self.groups)
