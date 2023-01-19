import multiprocessing

import asyncio
import json
import sys

from src.uni_group_tool.Front_end.tk_front import App
from uni_group_tool.main import groups_to_csv, run
multiprocessing.freeze_support()

if __name__ == "__main__":

    if len(sys.argv) > 1:
        data = json.loads(sys.argv[2])
        result_path = sys.argv[3] + '/results.json'
        size_of_teams = data["size_of_teams"]
        criteria = data["criteria"]
        shuffle = data["shuffle"]
        weights = data["weights"]
        data_path = data["data_path"]
        debugging = data["debugging"]
        saving = data["saving"]
        min_group_size_or_amount_of_groups = data["min_group_size_or_amount_of_groups"]

        for i in run(criteria, size_of_teams, shuffle, weights, data_path, False, saving,
                     min_group_size_or_amount_of_groups):
            if isinstance(i[0], int):
                with open(result_path, 'w', encoding='utf-8') as f:
                    # json.dump({"loop": i[0]}, f, ensure_ascii=False, indent=4)
                    json.dump({"loop": i[0], "current": groups_to_csv(i[1])}, f, ensure_ascii=False, indent=4)
            else:
                with open(result_path, 'w', encoding='utf-8') as f:
                    json.dump({"answer": groups_to_csv(i[0])}, f, ensure_ascii=False, indent=4)

    else:
        # f = open("demofile1.txt", "a")
        # f.write("running  front end\n")
        # f.close()
        asyncio.run(App().exec())