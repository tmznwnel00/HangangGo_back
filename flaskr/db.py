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
        "storageBucket": "hanganggo-88a45.appspot.com",
    },
)

bucket = storage.bucket()

species_map = db.reference("/species_map")
species = db.reference("/species")
collection = db.reference("/collection")
photo = db.reference("/photo")
section = db.reference("/section")

# data = {
#     "user_id" : "1",
#     "storage_path" : "gs://hanganggo-88a45.appspot.com/sample.webp",
#     "rank1" : "Ardea alba",
#     "rank2" : "Ardea alba modesta",
#     "rank3" : "Ardea cocoi",
#     "createdAt" :  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#     "updatedAt" :  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
# }

data = {
    "species": [
        {
            "category": "식물",
            "speciesName": "아까시나무",
            "imgLink": "gs://hanganggo-88a45.appspot.com/species2.jpeg",
            "remark": "군락",
            "lat": 37,
            "lng": 126,
        },
        {
            "id": 3,
            "category": "식물",
            "speciesName": "물억새",
            "imgLink": "gs://hanganggo-88a45.appspot.com/Miscanthus_sacchariflorus.jpg",
            "remark": "군락",
            "lat": 40,
            "lng": 130,
        },
        {
            "id": 4,
            "category": "어류",
            "speciesName": "누치",
            "imgLink": "gs://hanganggo-88a45.appspot.com/Hemibarbus_labeo.JPG",
            "remark": "우점",
            "lat": 45,
            "lng": 146,
        },
        {
            "id": 5,
            "category": "어류",
            "speciesName": "가시납지리",
            "imgLink": "gs://hanganggo-88a45.appspot.com/species5.jpeg",
            "remark": "우점",
            "lat": 50,
            "lng": 110,
        },
        {
            "id": 6,
            "category": "육상곤충",
            "speciesName": "양봉꿀벌",
            "imgLink": "gs://hanganggo-88a45.appspot.com/Apis_mellifera.jpeg",
            "remark": "우점",
            "lat": 55,
            "lng": 106,
        },
        {
            "id": 7,
            "category": "육상곤충",
            "speciesName": "섬서구메뚜기",
            "imgLink": "gs://hanganggo-88a45.appspot.com/Atractomorpha_lata.jpeg",
            "remark": "우점",
            "lat": 30,
            "lng": 90,
        },
        {
            "id": 8,
            "category": "조류",
            "speciesName": "청둥오리",
            "imgLink": "gs://hanganggo-88a45.appspot.com/Anas_platyrhynchos.jpeg",
            "remark": "우점",
            "lat": 40,
            "lng": 146,
        },
        {
            "id": 9,
            "category": "조류",
            "speciesName": "황조롱이",
            "imgLink": "gs://hanganggo-88a45.appspot.com/Falco_tinnunculus.jpeg",
            "remark": "법적보호종",
            "lat": 48,
            "lng": 136,
        },
        {
            "id": 10,
            "category": "양서파충류",
            "speciesName": "참개구리",
            "imgLink": "gs://hanganggo-88a45.appspot.com/Pelophylax_nigromaculatus.jpeg",
            "remark": "우점",
            "lat": 50,
            "lng": 190,
        },
        {
            "id": 11,
            "category": "양서파충류",
            "speciesName": "옴개구리",
            "imgLink": "gs://hanganggo-88a45.appspot.com/Glandirana_emeljanovi.jpeg",
            "remark": "우점",
            "lat": 25,
            "lng": 126,
        },
    ],
}

data2 = {
    "category": "양서파충류",
    "speciesName": "줄장지뱀",
    "imgLink": "gs://hanganggo-88a45.appspot.com/Takydromus_wolteri.jpeg",
    "remark": "우점",
    "lat": 25,
    "lng": 126,
    "hangang_alphabet": "R",
    "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}

species_map.push(data2)
