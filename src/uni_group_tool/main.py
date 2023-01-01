# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import math
import multiprocessing

from uni_group_tool.students import student
from uni_group_tool.One_Group import Group
from uni_group_tool.Many_Groups import Groups
from typing import List
import copy
import random


# def display_csv(path: str):
#     df = pd.read_csv(path)
#     print(df)


def get_csv(path: str):
    with open(path, newline='') as csvfile:
        file = csv.DictReader(csvfile)
        return list(file)

def get_csv_table_students(path: str):
    file1 = open(path, 'r')
    Lines = file1.readlines()
    all_line = []
    # Strips the newline character
    for line in Lines:
        all_line.append((line.split(",")[0:2])+[line.split(",")[7]])
    #print(all_line)
    return all_line



def save_csv(csv_input: dict[str | int, dict[str, str]]):
    keys = csv_input[0].keys()

    with open('test_data/groups_front_end.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)   # type: ignore
        dict_writer.writeheader()
        dict_writer.writerows(csv_input)    # type: ignore


def extract_csv_data(csv_input):
    # print(csv_input)
    for i in csv_input:
        print(i["Names"])


def initialize(csv_input:  dict[str | int, dict[str, str]], group_size: int, shuffle: bool,min_group_size_or_amount_of_groups:bool):
    if min_group_size_or_amount_of_groups:
        number_of_groups = int(math.floor(len(csv_input) / group_size))
    else:
        number_of_groups = group_size
    total = 0
    if shuffle:
        random.shuffle(csv_input)   # type: ignore
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


# def csv_to_students(csv_input: dict[str| int,dict[str,str]]):
#     students = []
#     for i in csv_input:
#         students.append(
#             student(i["StudentID"], i["username"], i["surname"], i["firstName"], i["gender"], i["home"],
#                     i["average"], i["team"], i["status"]))
#     return students


def students_to_csv(students_object: List[student], team: int):
    students = []
    for i in students_object:
        students.append(
            {"StudentID": i.studentid, "username": i.username, "surname": i.surname, "firstName": i.firstName,
             "gender": i.gender,
             "home": i.home, "average": i.average, "team": team, "status": i.status})
    return students


def groups_to_csv(groups_object: Groups):
    students = []   # type: List[Group]
    for group in groups_object.get_groups():
        students = students + (students_to_csv(group.get_students(), group.group_number))
    return students


# def groups_to_students(all_teams: Groups):
#     groups_array = all_teams.get_groups()
#     for i in groups_array:
#         print("group number: ", i.group_number)
#         print("group size: ", i.group_size())
#         print("students: ", (students_to_csv(i.get_students())))
#         print("")

def compare_fitness(teams1: Groups, teams2: Groups, weights: dict[str, int]):
    temp = {teams1: {}, teams2: {}}   # type: dict[Groups,dict[str,int]]

    def collect_comparisons(d, order):
        for k, v in d.items():
            if isinstance(v, dict):
                collect_comparisons(v, order)
            else:
                if v is not None:
                    temp[order][k] = v

    overall_fitness1 = teams1.fitness.get_all()
    overall_fitness2 = teams2.fitness.get_all()
    collect_comparisons(overall_fitness1, teams1)
    collect_comparisons(overall_fitness2, teams2)
    #print(temp)
    score1 = 0  # type: float
    score2 = 0  # type: float
    for i, j in zip(temp[teams1], temp[teams2]):
        weight = weights.get([k for (k, v) in temp[teams1].items() if v == temp[teams1][i]][0])
        #print(weight,[k for (k, v) in temp[teams1].items() if v == temp[teams1][i]][0])
        if weight is None:
            weight = .6
        if temp[teams1][i] > temp[teams2][j]:
            score1 += 1 * weight
            if temp[teams1][j] != 0:
                score2 += (temp[teams2][i] / temp[teams1][j]) * weight
        if temp[teams1][i] < temp[teams2][j]:
            score2 += 1 * weight
            if temp[teams2][j] != 0:
                score1 += (temp[teams1][i] / temp[teams2][j]) * weight
    # print(score1, score2)
    if score1 > score2:
        return True, teams1
    else:
        return False, teams2


def overall_fitness(all_teams: Groups, modifed_groups_numbers: tuple[int, int], criteria: dict[str, list[str | tuple[str, str, int] | tuple[int, int]]]):
    groups = Groups([])
    for i in modifed_groups_numbers:
        groups.add_group(all_teams.get_groups()[i])

    fitness(groups, criteria)
    all_teams.many_groups_fitness()


def fitness(modifed_groups: Groups, criteria: dict[str, list[str | tuple[str, str, int] | tuple[int, int]]]):
    for key in criteria:
        # print("key", key)
        for item in criteria[key]:
            # print(key, item)
            modifed_groups.covert(key, item)
    return modifed_groups


def generate(org: Groups, best_team: Groups, current_time: int, criteria, weights):
    tabu_distance = 5
    neighbours = []
    for group1 in range(0, org.number_of_groups()):
        for student1 in range(0, org.get_groups()[group1].group_size()):
            for group2 in range(0, org.number_of_groups()):
                for student2 in range(0, org.get_groups()[group2].group_size()):
                    if group1 != group2:
                        if group2 > group1:
                            # modified_group = copy.deepcopy(org)
                            tabu = False
                            org.swap_students(group1, group2, student1, student2)
                            overall_fitness(org, (group1, group2), criteria)
                            # print(students_to_csv(org.get_groups()[group1].get_students()))
                            # print(students_to_csv(org.get_groups()[group2].get_students()))

                            if current_time - org.get_groups()[group1].get_student(
                                    student1).tabu_time < tabu_distance or current_time - \
                                    org.get_groups()[group2].get_student(student2).tabu_time < tabu_distance:
                                tabu = True
                            # if current_time > 14:
                            #     print(tabu)
                            asp = compare_fitness(org, best_team, weights)[0]
                            if not tabu or asp:
                                neighbours.append((copy.deepcopy(org), group1, group2, student1, student2))
                            # undo the swap for speed?
                            org.swap_students(group1, group2, student1, student2)
                            overall_fitness(org, (group1, group2), criteria)
                            # return
                        # print("first pair", group1, student1, "second pair", group2, student2)
    return neighbours


def sub_section_generate(segments):
    neighbours = []
    group = segments[0]
    org = segments[1]
    best_team = segments[2]
    current_time = segments[3]
    criteria = segments[4]
    weights = segments[5]
    tabu_distance = segments[6]
    for group1 in group:
        for student1 in range(0, org.get_groups()[group1].group_size()):
            for group2 in range(0, org.number_of_groups()):
                for student2 in range(0, org.get_groups()[group2].group_size()):
                    if group1 != group2:
                        if group2 > group1:
                            # modified_group = copy.deepcopy(org)
                            tabu = False
                            org.swap_students(group1, group2, student1, student2)
                            overall_fitness(org, (group1, group2), criteria)
                            # print(students_to_csv(org.get_groups()[group1].get_students()))
                            # print(students_to_csv(org.get_groups()[group2].get_students()))

                            if current_time - org.get_groups()[group1].get_student(
                                    student1).tabu_time < tabu_distance or current_time - \
                                    org.get_groups()[group2].get_student(student2).tabu_time < tabu_distance:
                                tabu = True
                            asp = compare_fitness(org, best_team, weights)[0]
                            # print(org.get_groups()[group1])
                            if not tabu or asp:
                                if org.get_groups()[group1].get_student(student1).get_all() != org.get_groups()[group2].get_student(student2).get_all():
                                    neighbours.append((copy.deepcopy(org), group1, group2, student1, student2))
                                # else:
                                #     print(org.get_groups()[group1].get_student(student1).get_all(),org.get_groups()[group2].get_student(student2).get_all())
                            # undo the swap for speed?
                            org.swap_students(group1, group2, student1, student2)
                            overall_fitness(org, (group1, group2), criteria)
    # print("done", group, sys.getsizeof(neighbours))
    return neighbours


def generate_multiprocessing(org: Groups, best_team: Groups, current_time: int, criteria, weights):
    # time_pre_multi_start = time.time()
    tabu_distance = 10
    # segments = [
    #     (x, org, best_team, current_time, criteria, weights, tabu_distance)
    #     for x in range(0, org.number_of_groups())]

    segments = [
        ([x], org, best_team, current_time, criteria, weights, tabu_distance)
        for x in range(0, org.number_of_groups())]

    with multiprocessing.Pool() as pool:
        neighbours = pool.map(sub_section_generate, segments)
    flat_list = [item for sublist in neighbours for item in sublist]
    return flat_list


def select(neighbours: List[tuple[Groups, tuple[int, int, int, int]]], weights):
    best = neighbours[0]
    if len(neighbours) != 1:
        for group in neighbours[1:]:
            comparison = compare_fitness(group[0], best[0], weights)
            if comparison[0]:
                best = group
    return best


def test(group_to_test, current_best_group, current_time, time_when_best_was_found, weights):
    if compare_fitness(group_to_test, current_best_group, weights)[0]:
        return group_to_test, current_time
    return current_best_group, time_when_best_was_found


def update(best_neighbour, current_time):
    # print(best_neighbour)
    group1 = best_neighbour[1]
    group2 = best_neighbour[2]
    student1 = best_neighbour[3]
    student2 = best_neighbour[4]
    best_neighbour[0].get_groups()[group1].get_student(student1).tabu_time = current_time
    best_neighbour[0].get_groups()[group2].get_student(student2).tabu_time = current_time
    current_time += 1
    return best_neighbour[0], current_time


def stop(current_time, time_when_best_was_found):
    if current_time - time_when_best_was_found > 20:
        # print("not done")
        return True
    return False


def score_custom():
    pass


def run(criteria, size_of_teams, shuffle, weights, data_path, debugging, saving,min_group_size_or_amount_of_groups):

    # check tomorrow
    # in generating nothing should be passing asp by the end
    # user input section
    # criteria = {"diversity": ["average", "home", "gender"],
    #             "amount_to_be_together": [("gender", "F", 2), ("gender", "M", 1), ("home", "O", 2), ("home", "H", 1)],
    #             "specific_teams": [[("208026943", 3), ("208063956", 3), ("207069131", 4)]]}

    # critera for diverse average, 2 females together and 2 online together, and 3 students in specific groups
    #print("not creashed")
    csv_input = get_csv(data_path)
    current_all_team = Groups(initialize(csv_input, size_of_teams, shuffle,min_group_size_or_amount_of_groups))
    # get the overall fitness of the whole thing
    overall_fitness(current_all_team, (range(0, current_all_team.number_of_groups())), criteria)  # type: ignore

    # starting variables initializing
    best_team = copy.deepcopy(current_all_team)
    current_time = 0
    time_when_best_was_found = current_time

    # running the optimisation
    while not stop(current_time, time_when_best_was_found):
        neighbours = generate_multiprocessing(current_all_team, best_team, current_time, criteria, weights)
        best_neighbour = select(neighbours, weights)
        best_team, time_when_best_was_found = test(best_neighbour[0], best_team, current_time,
                                                   time_when_best_was_found, weights)

        current_all_team, current_time = update(best_neighbour, current_time)
        yield current_time
        if debugging:
            print("best     ", best_team.fitness.get_all(), time_when_best_was_found, )
            print("neighbour", best_neighbour[0].fitness.get_all(), "group1", best_neighbour[1], "group2",
                  best_neighbour[2], "student1", best_neighbour[3], "student2", best_neighbour[4])
            print("current  ", current_all_team.fitness.get_all())
            print("")
    if saving:
        save_csv(groups_to_csv(best_team))
    yield best_team


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    criteria = {"diversity": ["average", "gender"],
                "amount_to_be_together": [("gender", "F", 2), ("home", "O", 2)],
                "specific_teams": [[("208026943", 3), ("208063956", 3), ("207069131", 4)]]}
    size_of_teams = 3
    shuffle = True
    weights =  {'gender': .2, 'average': .8, 'F': .2, 'O': .2, 'has_required_students': .2}

    data_path = "test_data/sample_short.csv"
    debugging = False
    saving = True
    for i in run(criteria, size_of_teams, shuffle, weights, data_path, debugging, saving,True):
        print(i)
