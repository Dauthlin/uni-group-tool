class group:
    def __init__(self, group_number):
        self.students = []
        self.group_number = group_number

    def get_students(self):
        return self.students

    def get_student(self, position):
        return self.students[position]

    def add_students(self, student):
        self.students.append(student)

    def group_size(self):
        return len(self.students)

    def remove_student(self, position):
        return self.students.pop(position)

    def replace(self, position, replacement):
        student = self.students[position]
        self.students[position] = replacement
        return student
