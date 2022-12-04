from students import student
from One_Group import Group
from typing import List
from Fitness_Data import FitnessData


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

    def get_fitness(self, type_of_fitness: tuple):
        result = []
        for single_group in self.groups:
            if type_of_fitness[0] == "diversity":
                result.append((single_group, single_group.get_fitness().get_diversity(type_of_fitness[1])))
        return result

    def diversity(self, type_of_diversity: str) -> int:

        for single_group in self.groups:
            total = 0
            for student1 in single_group.get_students():
                for student2 in single_group.get_students():
                    if student1 != student2:
                        # print(student1.surname, student2.surname, single_group.group_number)
                        if type_of_diversity == "average":
                            total += abs(student1.average - student2.average)
            single_group.get_fitness().set_diversity(type_of_diversity, total)
            # print(single_group.get_fitness().get_diversity(type_of_diversity))
