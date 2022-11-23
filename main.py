# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import pandas as pd


def get_csv(path):
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def display_csv(path):
    df = pd.read_csv(path)
    print(df)


def return_csv(path):
    with open(path, newline='') as csvfile:
        return csv.DictReader(csvfile)


def save_csv(csv_input):
    with open('test_data\groups.csv', mode='w') as groups:
        employee_writer = csv.writer(groups, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(csv_input)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_path = "test_data\data.csv"
    # get_csv(data_path)
    # save_csv(return_csv(get_csv(data_path)))
    display_csv(data_path)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
