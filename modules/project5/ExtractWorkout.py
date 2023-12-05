from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()

def extract_workout(content):
    prompt = 'You extract data about a workout, you create a name for it, and format it in the following JSON format: {"name":"Workout name", "exercises":[{"name":"Exercise name", "sets":5, "reps":5, "weights":225, "notes":"Heavy"}]}'
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": content}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=messages,
    )
    return json.loads(response.choices[0].message.content)
