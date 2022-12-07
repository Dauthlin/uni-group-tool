from students import student
from One_Group import Group
from typing import List
from Fitness_Data import FitnessData
import copy
from functools import reduce


class Groups:
    def __init__(self, all_groups: List[Group]):
        self.fitness = FitnessData()
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
            if type_of_fitness[0] == "diversity":  # ("diversity", "average")
                result.append((single_group, single_group.get_fitness().get_diversity(type_of_fitness[1])))
            if type_of_fitness[0] == "specific_teams":  # [("208026943", 3), ("208063956", 3), ("207069131", 4)]
                result.append((single_group, single_group.get_fitness().get_has_required_students()))
            if type_of_fitness[0] == "amount_to_be_together":  # ("minimum_of_type", "gender", "M")
                result.append(
                    (single_group,
                     single_group.get_fitness().get_should_be_together(type_of_fitness[1], type_of_fitness[2])))

        return result

    def many_groups_fitness(self):

        def merge_dict(dict1, dict2):
            for key, val in dict1.items():
                if type(val) == dict:
                    if key in dict2 and type(dict2[key] == dict):
                        merge_dict(dict1[key], dict2[key])
                else:
                    if key in dict2:
                        if dict1[key] is None or dict1[key] is None:
                            pass
                        else:
                            dict1[key] = dict2[key] + dict1[key]

            for key, val in dict2.items():
                if not key in dict1:
                    dict1[key] = val

            return dict1

        many_fitness = [single_group.get_fitness().get_all() for single_group in self.groups]
        combined_dict = copy.deepcopy(many_fitness[0])
        for i in many_fitness[1:]:
            combined_dict = merge_dict(combined_dict, i)
        #print(combined_dict)
        self.fitness.set_all(combined_dict)

        return self.fitness.get_all()
        #print(self.fitness.get_all())


    def amount_to_be_together(self, minimum_type: str, which_type: str, minimum_number: int):
        for single_group in self.groups:
            total = 0
            # each type in group in required minimum type
            if minimum_type == "gender":
                in_group = [single_student.gender for single_student in single_group.get_students() if
                            single_student.gender == which_type]
            if minimum_type == "home":
                in_group = [single_student.home for single_student in single_group.get_students() if
                            single_student.home == which_type]
            if len(in_group) == 0:
                total += 1
            elif len(in_group) < minimum_number:
                total += 0
            else:
                total += 1
            single_group.get_fitness().set_should_be_together(minimum_type, which_type, total)

    def specific_teams(self, studentid_to_group_number_list: List[tuple]):
        for single_group in self.groups:
            total = 0
            for studentid_to_group_number in studentid_to_group_number_list:
                # if student is meant to be in this group
                if single_group.group_number == studentid_to_group_number[1]:
                    # get all student  ID's in the group
                    ids_in_group = [single_student.studentid for single_student in single_group.get_students()]
                    # if the student is in the group +1 otherwise -1
                    if studentid_to_group_number[0] in ids_in_group:
                        total += 1
                    else:
                        total += -1
                    # print(studentid_to_group_number)

            single_group.get_fitness().set_has_required_students(total)

    def diversity(self, type_of_diversity: str):
        def convert_to_number(type_of_diversity_result: str):
            if (type_of_diversity_result == "H") or (type_of_diversity_result == "M"):
                return 1
            else:
                return 0

        for single_group in self.groups:
            total = 0
            for student1 in single_group.get_students():
                for student2 in single_group.get_students():
                    if student1 != student2:
                        # print(student1.surname, student2.surname, single_group.group_number)
                        if type_of_diversity == "average":
                            total += abs(student1.average - student2.average)
                        if type_of_diversity == "home":
                            total += abs(convert_to_number(student1.home) - convert_to_number(student2.home))
                            # print(total,student1.username,convert_to_number(student1.home),student2.username,convert_to_number(student2.home))
                        if type_of_diversity == "gender":
                            total += abs(convert_to_number(student1.gender) - convert_to_number(student2.gender))

            single_group.get_fitness().set_diversity(type_of_diversity, total)
            # print(single_group.get_fitness().get_diversity(type_of_diversity))
