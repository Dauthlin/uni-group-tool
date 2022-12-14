from flask import Flask, request , jsonify
from uni_group_tool.main import groups_to_csv, run


app = Flask(__name__)
app.config["DEBUG"] = True
# http://192.168.11.61:5000
# curl -i -H "Content-Type: application/json" -X POST -d '{"size_of_teams":8,"shuffle":true,"criteria":{"diversity":["average","gender"],"amount_to_be_together":[["gender","F",2],["home","O",2]],"specific_teams":[[["208026943",3],["208063956",3],["207069131",4]]]},"weights":{},"data_path":"test_data/sample.csv","debugging":false,"saving":true}' http://192.168.11.61:5000/run_program
@app.route('/run_program', methods=['GET','POST'])
def run_program():
    data = request.json
    # parsing data
    size_of_teams = data["size_of_teams"]
    criteria = data["criteria"]
    shuffle = data["shuffle"]
    weights = data["weights"]
    data_path = data["data_path"]
    debugging = data["debugging"]
    saving = data["saving"]
    # run program
    best_team = run(criteria, size_of_teams, shuffle, weights, data_path, debugging,saving)
    return groups_to_csv(best_team)


if __name__ == '__main__':
    app.run(host='0.0.0.0')