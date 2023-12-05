from modules.project5.UserModel import UserModel
from modules.project5.Workout import get_workout
from modules.project5.ExtractWorkout import extract_workout, create_workout
import json

user_model = UserModel()
user_model.create_user('joe.finnell', 'Joe', 'Finnell')

# Add a workout to the user's workouts
gpt_workout_json = extract_workout("I did squats for 5 sets of 5 at 325 pounds it was heavy, I did bench for 6 by 6 at 225 it felt okay, curls 6 sets of 8 reps at 30lbs each arm")
if gpt_workout_json:
    workout = get_workout(gpt_workout_json)
    user_model.add_workout('joe.finnell', workout)


# Have GPT suggest a workout based on past workouts
past_workouts = user_model.get_user_workouts('joe.finnell')
gpt_suggested_workout = create_workout(json.dumps(past_workouts))

user_model.add_suggested_workout('joe.finnell', get_workout(gpt_suggested_workout))