import json
import sys
import ast

from uni_group_tool.main import groups_to_csv, run

if __name__ == "__main__":
    # Opening JSON file

    #data = ast.literal_eval(json_data)

    data = json.loads(sys.argv[1])
    size_of_teams = data["size_of_teams"]
    criteria = data["criteria"]
    shuffle = data["shuffle"]
    weights = data["weights"]
    data_path = data["data_path"]
    debugging = data["debugging"]
    saving = data["saving"]
    #print(data)

    for i in run(criteria, size_of_teams, shuffle, weights, data_path, False, saving):
        if isinstance(i, int):
            # with open('test_data/results.json', 'w', encoding='utf-8') as f:
            #     json.dump({"loop":i}, f, ensure_ascii=False, indent=4)
            print(json.dumps({"loop":i}))
        else:
            # with open('test_data/results.json', 'w', encoding='utf-8') as f:
            #     json.dump({"answer":groups_to_csv(i)}, f, ensure_ascii=False, indent=4)
            print(json.dumps({"answer":groups_to_csv(i)}))

    # with open('test_data/results.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)
