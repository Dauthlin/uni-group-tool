from students import student
from OneGroup import group


class groups:
    def __init__(self, allgroups):
        self.groups = allgroups

    def get_groups(self):
        return self.groups

    def add_group(self, single_group):
        self.groups.append(single_group)

    def number_of_groups(self):
        return len(self.groups)

    def swap_students(self, group1, group2, position1, position2):
        student1 = self.groups[group1].get_student(position1)
        student2 = self.groups[group2].get_student(position2)
        self.groups[group1].replace(position1, student2)
        self.groups[group2].replace(position2, student1)


