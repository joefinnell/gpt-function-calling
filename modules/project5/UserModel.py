import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class UserModel:
    def __init__(self):
        # Initialize Firebase Admin SDK
        cred = credentials.Certificate('/Users/joe.finnell/git/gpt-function-calling/creds-firebase.json')
        firebase_admin.initialize_app(cred)

        # Get Firestore client
        self.db = firestore.client()

    def create_user(self, user_id, first_name, last_name):
        # Create a new user document with a specific ID
        user_ref = self.db.collection('users').document(user_id)
        user_ref.set({
            'first_name': first_name,
            'last_name': last_name
        })

    def add_workout(self, user_id, workout):
        # Add a new workout document to the user's workouts subcollection
        user_ref = self.db.collection('users').document(user_id)
        workouts_ref = user_ref.collection('workouts').document()
        workouts_ref.set(workout.tojson())

    def add_suggested_workout(self, user_id, workout):
        # Add a new suggested workout document to the user's suggested workouts subcollection
        user_ref = self.db.collection('users').document(user_id)
        workouts_ref = user_ref.collection('suggested_workouts').document()
        workouts_ref.set(workout.tojson())

    def get_user_workouts(self, user_id):
        # Get all workouts for a specific user, sorted by date
        user_ref = self.db.collection('users').document(user_id)
        workouts_ref = user_ref.collection('workouts').order_by('date').get()
        workouts = [doc.to_dict() for doc in workouts_ref]
        return workouts
