import flask

from uni_group_tool.main import groups_to_csv, run

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# http://192.168.11.61:5000
@app.route('/run_program', methods=['GET'])
def run_program():
    criteria = {"diversity": ["average", "gender"],
                "amount_to_be_together": [("gender", "F", 2), ("home", "O", 2)],
                "specific_teams": [[("208026943", 3), ("208063956", 3), ("207069131", 4)]]}
    size_of_teams = 6
    shuffle = True
    weights = {}  # type: dict[str,int]
    data_path = "test_data/sample.csv"
    debugging = False
    saving = True
    best_team = run(criteria, size_of_teams, shuffle, weights, data_path, debugging,saving)
    return groups_to_csv(best_team)


if __name__ == '__main__':
    app.run(host='0.0.0.0')