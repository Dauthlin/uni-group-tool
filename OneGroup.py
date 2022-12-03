class group:
    def __init__(self, group_number):
        self.students = []
        self.group_number = group_number

    def get_students(self):
        return self.students

    def add_students(self, student):
        self.students.append(student)

    def group_size(self):
        return len(self.students)
