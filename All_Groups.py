from students import student
from One_Group import Group
from typing import List


class Groups:
    def __init__(self, all_groups: List[Group]):
        self.groups = all_groups

    def get_groups(self) -> List[Group]:
        return self.groups

    def add_group(self, single_group: Group):
        self.groups.append(single_group)

    def number_of_groups(self) -> int:
        return len(self.groups)

    def swap_students(self, group1: int, group2: int, position1: int, position2: int):
        student1 = self.groups[group1].get_student(position1)
        student2 = self.groups[group2].get_student(position2)
        self.groups[group1].replace(position1, student2)
        self.groups[group2].replace(position2, student1)
