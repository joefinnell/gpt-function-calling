import os
import requests
from dotenv import load_dotenv

BASE_URL = "https://api.calendly.com"
API_KEY = os.environ.get("CALENDLY_API_TOKEN")


class CalendlyAPI:
    """A wrapper around the Calendly API"""
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }


    def build_url(self, endpoint):
        return BASE_URL + endpoint


    def make_request(self, method, url, params=None, payload=None):
        try:
            response = requests.request(method, url, headers=self.headers, params=params, json=payload)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None


    def get_user_schedule_availability(self):
        """Get a user's schedule availability"""
        url = self.build_url("/user_availability_schedules")
        params = {
            "user": self.get_current_user_uri(),
        }
        return self.make_request("GET", url, params=params)


    def create_scheduling_link(self):
        """Get a scheduling link"""
        url = self.build_url("/scheduling_links")
        payload = {
            "max_event_count": 1,
            "owner": self.get_event_uri(),
            "owner_type": "EventType"
        }
        response = self.make_request("POST", url, payload=payload)
        return response["resource"]["booking_url"] if response else None


    def get_event_uri(self):
        """Get the URI for the test event"""
        event_types = self.list_users_event_types()["collection"]
        for event_type in event_types:
            if event_type["name"] == "Test Event":
                return event_type["uri"]
        return None


    def list_users_event_types(self):
        """List a user's event types"""
        url = self.build_url("/event_types")
        params = {
            "user": self.get_current_user_uri(),
        }
        return self.make_request("GET", url, params=params)


    def get_current_user_uri(self):
        """Get the URI for the current user"""
        url = self.build_url("/users/me")
        response = self.make_request("GET", url)
        return response["resource"]["uri"] if response else None
