class Student:
    def __init__(self, name, ID, score=[]):
        self.name = name
        self.ID = ID
        self.score = score

    @property
    def average(self):
        return sum(self.score) / len(self.score) if self.score else 0

    def add_score(self, score):
        self.score.append(score)

    def __str__(self):
        return f"Student(ID: {self.ID}, Name: {self.name}, Average Score: {self.average})"
