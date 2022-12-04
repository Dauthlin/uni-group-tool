from students import student


class Group:
    def __init__(self, group_number: int):
        self.students = []
        self.group_number = group_number

    def get_students(self):
        return self.students

    def get_student(self, position: int) -> student:
        return self.students[position]

    def add_student(self, new_student: student):
        self.students.append(new_student)

    def group_size(self) -> int:
        return len(self.students)

    def remove_student(self, position: int) -> student:
        return self.students.pop(position)

    def replace(self, position: int, replacement: student):
        self.students[position] = replacement


