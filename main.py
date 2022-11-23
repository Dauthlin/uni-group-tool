# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import pandas as pd




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
    #print(csv_input)
    for i in csv_input:
        print(i["Names"])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_path = "test_data\data.csv"
    #extract_csv_data(get_csv(data_path))
    #print(get_csv(data_path))


    save_csv(get_csv(data_path))
