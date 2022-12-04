from students import student
from Fitness_Data import FitnessData

class Group:
    def __init__(self, group_number: int):
        self.students = []
        self.group_number = group_number
        self.fitness = FitnessData()

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

    def get_fitness(self) -> FitnessData:
        return self.fitness

    def set_fitness(self, new_fitness: FitnessData):
        self.fitness = new_fitness



