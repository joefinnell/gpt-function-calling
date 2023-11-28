import json
import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

BASE_URL = "https://api.calendly.com"
API_KEY = os.environ.get("CALENDLY_API_TOKEN")


def build_url(endpoint):
    return BASE_URL + endpoint

def get_headers():
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

def get_user_schedule_availability():
    """Get a user's schedule availability"""
    url = build_url("/user_availability_schedules")
    params = {
        "user": get_current_user_uri(),
    }
    try:
        response = requests.get(url, headers=get_headers(), params=params)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def create_scheduling_link():
    """Get a scheduling link"""
    url = build_url("/scheduling_links")
    payload = {
        "max_event_count": 1,
        "owner": get_event_uri(),
        "owner_type": "EventType"
    }
    try:
        response = requests.post(url, headers=get_headers(), json=payload)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        return response.json()["resource"]["booking_url"]
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def get_event_uri():
    """Get the URI for the test event"""
    event_types = list_users_event_types()['collection']
    for event_type in event_types:
        if event_type['name'] == 'Test Event':
            return event_type['uri']
    return None

def list_users_event_types():
    """List a user's event types"""
    url = build_url("/event_types")
    params = {
        "user": get_current_user_uri(),
    }
    try:
        response = requests.get(url, headers=get_headers(), params=params)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_current_user_uri():
    """Get the URI for the current user"""
    url = build_url("/users/me")
    try:
        response = requests.get(url, headers=get_headers())
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        return response.json()["resource"]["uri"]
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def get_bike_inventory():
    {}

def get_tools():
    return [
        {
            "type": "function",
            "function": {
                "name": "get_user_schedule_availability",
                "description": "Returns a the assistants schedule availability when asked what times they are available",
                "parameters": {
                    "type": "object",
                    "properties": {
                    },
                    "required": [],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "create_scheduling_link",
                "description": "Creates a secheduling link that allows a user to set up a meeting with the assistant",
                "parameters": {
                    "type": "object",
                    "properties": {
                    },
                    "required": [],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "dummy_function",
                "description": "A dummy function that does nothing",
                "parameters": {
                    "type": "object",
                    "properties": {
                    },
                    "required": [],
                },
            },
        },
    ]

def dummy_function():
    return "dummy function"

def get_available_functions():
    return {
            "get_user_schedule_availability": get_user_schedule_availability,
            "create_scheduling_link": create_scheduling_link,
            "dummy_function": dummy_function,
        } 

def run_conversation():
    # Step 1: send the conversation and available functions to the model
    messages = [{"role": "user", "content": "Can we set up a meeting?"}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=get_tools(),
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    # Step 2: check if the model wanted to call a function
    if tool_calls:
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = get_available_functions() 
        messages.append(response_message)  # extend conversation with assistant's reply
        # Step 4: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_response = function_to_call()
            print(function_response)

run_conversation()
    