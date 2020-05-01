
import coursegenerator
import course_structures
import pyrebase
import json
from datetime import datetime
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import db

config = {
  "apiKey": "AIzaSyDyJ08AU94tm8Qi9nownWCSN1tLw3Oj4Kk",
  "authDomain": "advisor-c0b7d.firebaseapp.com",
  "databaseURL": "https://advisor-c0b7d.firebaseio.com",
  "storageBucket": "advisor-c0b7d.appspot.com",
  "serviceAccount": "advisor-c0b7d-firebase-adminsdk-nx4r4-adc5a434c9.json"
}

"""firebase admin credentials
cred = credentials.Certificate('advisor-c0b7d-firebase-adminsdk-nx4r4-adc5a434c9.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://advisor-c0b7d.firebaseio.com'
})
"""

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db1 = firebase.database()

def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        gensched()

def gensched():
    classargs = db1.child("Classes/classargs/").get()
    semArg = classargs.val()['type']
    if semArg == 'Spring':
        semester = course_structures.Semester(True)
    else:
        semester = course_structures.Semester(False)
    with open('classargs.json', 'w') as json_file:
        json.dump(classargs.val(), json_file)
    targets = coursegenerator.genSchedules(semester.df1, 'classargs.json')
    coursegenerator.rankPng(targets, 3, alg = 3, pweight = 3, cweight = 1)

    path_on_cloud = "Schedules/solutions0.png"
    path_local = "solutions0.png"
    storage.child(path_on_cloud).put(path_local)
    path_on_cloud = "Schedules/solutions1.png"
    path_local = "solutions1.png"
    storage.child(path_on_cloud).put(path_local)
    path_on_cloud = "Schedules/solutions2.png"
    path_local = "solutions2.png"
    storage.child(path_on_cloud).put(path_local)

def stream_handler(msg):
    gensched()
    print("updated")

def main():
    my_stream = db1.child("Classes/classargs/").stream(stream_handler)

if __name__ == "__main__":
    main()
