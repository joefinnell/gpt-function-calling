from modules.project5.UserModel import UserModel
from modules.project5.Workout import Workout, Exercise
from modules.project5.ExtractWorkout import extract_workout

user_model = UserModel()
user_model.create_user('joe.finnell', 'Joe', 'Finnell')

# workout = Workout('Leg Day', '2023-12-04')
# workout.add_exercise(Exercise('Squat', 5, 5, 225, 'Heavy'))
# workout.add_exercise(Exercise('Leg Press', 5, 5, 450, 'Heavy'))
# workout.add_exercise(Exercise('Leg Curl', 5, 5, 120, 'Heavy'))
# workout.add_exercise(Exercise('Leg Extension', 5, 5, 120, 'Heavy'))


gpt_workout = extract_workout("I did squats for 5 sets of 5 at 325 pounds it was heavy, I did bench for 6 by 6 at 225 it felt okay, curls 6 sets of 8 reps at 30lbs each arm")
if gpt_workout:
    print(gpt_workout)
    workout = Workout(gpt_workout['name'])
    for exercise in gpt_workout['exercises']:
        workout.add_exercise(Exercise(exercise['name'], exercise['sets'], exercise['reps'], exercise['weights'], exercise['notes']))
    user_model.add_workout('joe.finnell', workout)

print(user_model.get_user_workouts('joe.finnell'))
