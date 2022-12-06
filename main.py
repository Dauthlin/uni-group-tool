# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import pandas as pd
import numpy as np
import random
from students import student
from One_Group import Group
from Many_Groups import Groups
from typing import List


def display_csv(path: str):
    df = pd.read_csv(path)
    print(df)


def get_csv(path: str):
    with open(path, newline='') as csvfile:
        file = csv.DictReader(csvfile)
        return list(file)


def save_csv(csv_input: dict):
    keys = csv_input[0].keys()

    with open('test_data\groups.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(csv_input)


def extract_csv_data(csv_input):
    # print(csv_input)
    for i in csv_input:
        print(i["Names"])


def initialize(csv_input: dict, group_size: int):
    number_of_groups = int(np.floor(len(csv_input) / group_size))
    total = 0
    # random.shuffle(csv_input)
    output_groups = []
    for i in range(1, number_of_groups + 1):
        output_groups.append(Group(i))
    while total != len(csv_input):
        for i in range(1, number_of_groups + 1):
            if total != len(csv_input):
                output_groups[i - 1].add_student(
                    student(csv_input[total]["StudentID"], csv_input[total]["username"], csv_input[total]["surname"],
                            csv_input[total]["firstName"], csv_input[total]["gender"], csv_input[total]["home"],
                            csv_input[total]["average"],
                            csv_input[total]["team"], csv_input[total]["status"]))

                total += 1

    return output_groups


def csv_to_students(csv_input: dict):
    students = []
    for i in csv_input:
        students.append(
            student(i["StudentID"], i["username"], i["surname"], i["firstName"], i["gender"], i["home"],
                    i["average"], i["team"], i["status"]))
    return students


def students_to_csv(students_object: List[student]):
    students = []
    for i in students_object:
        students.append(
            {"StudentID": i.studentid, "username": i.username, "surname": i.surname, "firstName": i.firstName,
             "gender": i.gender,
             "home": i.home, "average": i.average, "team": i.team, "status": i.status})
    return students


def groups_to_students(all_teams: Groups):
    groups_array = all_teams.get_groups()
    for i in groups_array:
        print("group number: ", i.group_number)
        print("group size: ", i.group_size())
        print("students: ", (students_to_csv(i.get_students())))
        print("")


def compare_fitness(teams1: Groups, teams2: Groups, weights: dict):
    temp = {1: {}, 2: {}}

    def collect_comparisons(d, order):
        for k, v in d.items():
            if isinstance(v, dict):
                collect_comparisons(v, order)
            else:
                if v is not None:
                    temp[order][k] = v

    overall_fitness1 = teams1.fitness.get_all()
    overall_fitness2 = teams2.fitness.get_all()
    collect_comparisons(overall_fitness1, 1)
    collect_comparisons(overall_fitness2, 2)

    score1 = 0
    score2 = 0
    for i, j in zip(temp[1], temp[2]):
        # print(temp[1][i], temp[2][j])
        if temp[1][i] > temp[2][j]:
            score1 += 1
        if temp[1][i] < temp[2][j]:
            score2 += 1
    print(score1, score2)
    if score1 > score2:
        return teams1
    else:
        return teams2


def overall_fitness(all_teams: Groups, modifed_groups_numbers: tuple, criteria: List[bool]):
    group1 = all_teams.get_groups()[modifed_groups_numbers[0]]
    group2 = all_teams.get_groups()[modifed_groups_numbers[1]]

    # groups 3 and 4 are for testing remove later
    group3 = all_teams.get_groups()[5]
    group4 = all_teams.get_groups()[6]

    changed_fitness1 = fitness(Groups([group1, group2]), criteria)
    changed_fitness2 = fitness(Groups([group3, group4]), criteria)
    # groups_to_students(changed_fitness2)
    print(compare_fitness(changed_fitness1, changed_fitness2, {}))


def fitness(modifed_groups: Groups, criteria: List[bool]):
    modifed_groups.diversity("average")
    # print(modifed_groups.get_fitness(("diversity", "average")))

    modifed_groups.specific_teams([("208026943", 3), ("208063956", 3), ("207069131", 4)])
    # print(modifed_groups.get_fitness(("specific_teams", "")))

    modifed_groups.amount_to_be_together("gender", "M", 2)
    # print(modifed_groups.get_fitness(("amount_to_be_together", "gender", "M")))
    modifed_groups.many_groups_fitness()

    # groups_to_students(modifed_groups)
    return modifed_groups


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_path = "test_data\sample.csv"
    # data_path = "test_data\data.csv"
    csv_input = get_csv(data_path)
    # extract_csv_data(get_csv(data_path))
    # print(get_csv(data_path))
    # save_csv(get_csv(data_path))
    AllTeams = Groups(initialize(csv_input, 3))
    best_team = AllTeams
    # single_group = AllTeams.get_groups()[0]
    # print(single_group.get_student(0))
    # AllTeams.swap_students(0, 1, 0, 0)
    # print(students_to_csv(single_group.get_students()))
    overall_fitness(AllTeams, (2, 3), [True])
    # groups_to_students(AllTeams)
    # save_csv(initialized_groups)
    # students = csv_to_students(csv_input)
    # print(students)
    # print(csv_input)
    # print(students_to_csv(students))
