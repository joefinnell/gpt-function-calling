import datetime
class Workout:
    def __init__(self, name, exercises = []):
        self.name = name
        self.date = datetime.date.today().strftime("%Y-%m-%d")
        self.exercises = exercises

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def remove_exercise(self, exercise):
        self.exercises.remove(exercise)

    def get_exercise(self, exercise):
        return self.exercises[exercise]

    def get_exercises(self):
        return self.exercises

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def set_name(self, name):
        self.name = name

    def set_date(self, date):
        self.date = date

    def __str__(self):
        return "Workout: " + self.name + " Date: " + self.date
    
    def tojson(self):
        return {
            'name': self.name,
            'date': self.date,
            'exercises': [e.tojson() for e in self.exercises]
        }

class Exercise:
    def __init__(self, name, sets, reps, weights, notes):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.weights = weights
        self.notes = notes

    def tojson(self):
        return {
            'name': self.name,
            'sets': self.sets,
            'reps': self.reps,
            'weights': self.weights,
            'notes': self.notes
        }