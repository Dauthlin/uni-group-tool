# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import pandas as pd
import numpy as np
import random
from students import student
from One_Group import Group
from All_Groups import Groups


def display_csv(path):
    df = pd.read_csv(path)
    print(df)


def get_csv(path):
    with open(path, newline='') as csvfile:
        file = csv.DictReader(csvfile)
        return list(file)


def save_csv(csv_input):
    keys = csv_input[0].keys()

    with open('test_data\groups.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(csv_input)


def extract_csv_data(csv_input):
    # print(csv_input)
    for i in csv_input:
        print(i["Names"])


def initialize(csv_input, group_size):
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


def csv_to_students(csv_input):
    students = []
    for i in csv_input:
        students.append(
            student(i["StudentID"], i["username"], i["surname"], i["firstName"], i["gender"], i["home"],
                    i["average"], i["team"], i["status"]))
    return students


def students_to_csv(students_object):
    students = []
    for i in students_object:
        students.append(
            {"StudentID": i.StudentID, "username": i.username, "surname": i.surname, "firstName": i.firstName,
             "gender": i.gender,
             "home": i.home, "average": i.average, "team": i.team, "status": i.status})
    return students


def groups_to_students(AllTeams):
    groups_array = AllTeams.get_groups()
    for i in groups_array:
        print("group number: ", i.group_number)
        print("group size: ", i.group_size())
        print("students: ", (students_to_csv(i.get_students())))
        print("")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_path = "test_data\sample.csv"
    # data_path = "test_data\data.csv"
    csv_input = get_csv(data_path)
    # extract_csv_data(get_csv(data_path))
    # print(get_csv(data_path))
    # save_csv(get_csv(data_path))
    AllTeams = Groups(initialize(csv_input, 19))
    best_team = AllTeams
    # single_group = AllTeams.get_groups()[0]
    # print(single_group.get_student(0))
    AllTeams.swap_students(0,1,0,0)
    # print(students_to_csv(single_group.get_students()))

    groups_to_students(AllTeams)
    # save_csv(initialized_groups)
    # students = csv_to_students(csv_input)
    # print(students)
    # print(csv_input)
    # print(students_to_csv(students))
