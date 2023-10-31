import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime

cred = credentials.Certificate(
    "hanganggo-88a45-firebase-adminsdk-97702-c4faccd7b0.json"
)

firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://hanganggo-88a45-default-rtdb.asia-southeast1.firebasedatabase.app/",
        "storageBucket": "hanganggo-88a45.appspot.com"
    },
)

bucket = storage.bucket()

species_map = db.reference("/species_map")
species = db.reference("/species")
collection = db.reference("/collection")
photo = db.reference("/photo")

data = {
    "user_id" : "1",
    "storage_path" : "gs://hanganggo-88a45.appspot.com/sample.webp",
    "rank1" : "Ardea alba",
    "rank2" : "Ardea alba modesta",
    "rank3" : "Ardea cocoi",
    "createdAt" :  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    "updatedAt" :  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
}

photo.push(data)
