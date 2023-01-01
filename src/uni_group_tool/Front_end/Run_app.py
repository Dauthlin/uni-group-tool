import json
import sys
import ast

from uni_group_tool.main import groups_to_csv, run

def run_main():
    # Opening JSON file

    # data = ast.literal_eval(json_data)

    data = json.loads(sys.argv[1])
    result_path = data["result_path"]
    size_of_teams = data["size_of_teams"]
    criteria = data["criteria"]
    shuffle = data["shuffle"]
    weights = data["weights"]
    data_path = data["data_path"]
    debugging = data["debugging"]
    saving = data["saving"]
    min_group_size_or_amount_of_groups = data["min_group_size_or_amount_of_groups"]
    # print(data)
    # f = open("C:\Users\Michael\OneDrive\uni\project\coding\output\data\demofile2.txt", "a")
    # f.write("Now the file has more content!")
    # f.close()
    for i in run(criteria, size_of_teams, shuffle, weights, data_path, False, saving,
                 min_group_size_or_amount_of_groups):
        if isinstance(i, int):
            with open(result_path, 'w', encoding='utf-8') as f:
                json.dump({"loop":i}, f, ensure_ascii=False, indent=4)
            #print(json.dumps({"loop": i}))
        else:
            with open(result_path, 'w', encoding='utf-8') as f:
                json.dump({"answer":groups_to_csv(i)}, f, ensure_ascii=False, indent=4)
            #print(json.dumps({"answer": groups_to_csv(i)}))

    # with open('test_data/results.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    run_main()
