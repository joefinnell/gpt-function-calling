from modules.project5.UserModel import UserModel
from modules.project5.Workout import get_workout
from modules.project5.ExtractWorkout import extract_workout, create_workout
from modules.project5.SpeechExtraction import get_text_from_speech
import json

user_model = UserModel()
user_model.create_user('joe.finnell', 'Joe', 'Finnell')

# Add a workout to the user's workouts
workout_text = get_text_from_speech('/Users/joe.finnell/git/gpt-function-calling/audio/workout.m4a')
gpt_workout_json = extract_workout(workout_text)
if gpt_workout_json:
    workout = get_workout(gpt_workout_json)
    user_model.add_workout('joe.finnell', workout)


# Have GPT suggest a workout based on past workouts
past_workouts = user_model.get_user_workouts('joe.finnell')
gpt_suggested_workout = create_workout(json.dumps(past_workouts))

user_model.add_suggested_workout('joe.finnell', get_workout(gpt_suggested_workout))