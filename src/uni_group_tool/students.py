class student:
    import copy

    def __init__(self, studentID, username, surname, firstName, gender, home, average, team, status):
        self.studentid = studentID
        self.username = username
        self.surname = surname
        self.firstName = firstName
        self.gender = gender
        self.home = home
        self.average = int(average)
        self.team = team
        self.status = status
        self.tabu_time = -100

    def get_all(self):
        return [self.gender, self.home, self.average]
