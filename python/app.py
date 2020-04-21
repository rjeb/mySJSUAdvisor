import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('advisor-c0b7d-firebase-adminsdk-nx4r4-adc5a434c9.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://advisor-c0b7d.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('Classes/-M5OvQBHv4W3wrWdpmOy')
print(ref.get())