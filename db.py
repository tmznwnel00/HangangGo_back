import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('hanganggo-88a45-firebase-adminsdk-97702-c4faccd7b0.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': "https://hanganggo-88a45-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference('Database reference')

# ref.update({"user_id": 1, "name": "test"})