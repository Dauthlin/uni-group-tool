from students import student
from One_Group import Group
from typing import List
from Fitness_data import Fitness_data


class Groups:
    def __init__(self, all_groups: List[Group]):
        self.fitness = Fitness_data
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

    def get_fitness(self) -> Fitness_data:
        return self.fitness

    def set_fitness(self, new_fitness: Fitness_data):
        self.fitness = new_fitness

    def diversity(self) -> int:
        total = 0
        for single_group in self.groups:
            for student1 in single_group.get_students():
                for student2 in single_group.get_students():
                    if student1 != student2:
                        # print(student1.surname, student2.surname, single_group.group_number)
                        total += abs(student1.average - student2.average)
        return total
