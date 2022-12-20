from flask import Flask
from flask_sock import Sock
from uni_group_tool.main import groups_to_csv, run
import ast

app = Flask(__name__)
sock = Sock(app)


@sock.route('/run_program')
def run_program(sock):
    while True:
        data = None
        while data is None:
            data = sock.receive()
        data = ast.literal_eval(data)  # type: ignore
        size_of_teams = data["size_of_teams"]
        criteria = data["criteria"]
        shuffle = data["shuffle"]
        weights = data["weights"]
        data_path = data["data_path"]
        debugging = data["debugging"]
        saving = data["saving"]
        print(data)

        for i in run(criteria, size_of_teams, shuffle, weights, data_path, debugging, saving):
            print(i)
            if isinstance(i, int):
                sock.send({"loop":i})
            else:
                sock.send({"answer":groups_to_csv(i)})
        sock.send({"complete": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
