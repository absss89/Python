class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def calculate_average(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

class GradeBook:
    def __init__(self):
        self.students = []
        self.students_ids = set()

    def add_student(self, name, student_ids):