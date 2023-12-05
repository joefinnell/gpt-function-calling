from modules.project5.UserModel import UserModel
from modules.project5.Workout import Workout, Exercise

user_model = UserModel()
user_model.create_user('joe.finnell', 'Joe', 'Finnell')

workout = Workout('Leg Day', '2023-12-04')
workout.add_exercise(Exercise('Squat', 5, 5, 225, 'Heavy'))
workout.add_exercise(Exercise('Leg Press', 5, 5, 450, 'Heavy'))
workout.add_exercise(Exercise('Leg Curl', 5, 5, 120, 'Heavy'))
workout.add_exercise(Exercise('Leg Extension', 5, 5, 120, 'Heavy'))

user_model.add_workout('joe.finnell', workout)
print(user_model.get_user_workouts('joe.finnell'))