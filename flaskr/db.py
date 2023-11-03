import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime

cred = credentials.Certificate(
    # "hanganggo-88a45-firebase-adminsdk-97702-c4faccd7b0.json"
    "hanganggo-88a45-firebase-adminsdk-97702-1f415b24ed.json"
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
    "user_id": 1,
    "category": "자주괴불주머니",
    "korean_name": "식물",
    "imgLink": "gs://hanganggo-88a45.appspot.com/Corydalis_incisa_pers.jpeg",
    "remark": "기후변화 생물지표종",
    "lat": 25,
    "lng": 126,
    "hangang_alphabet": "Q",
    "description" : "기후변화 생물지표종으로 긴 타원형의 뿌리에서 여러 대의 줄기가 나와 20-50cm까지 자란다. 잎은 3-8cm로 길고 작은 잎이 3장씩 2번 갈라져 나온다. 그늘지고 축축한 땅에서 자라고 5월에 홍자색 꽃을 피우고 4-12cm까지 자란다.",
    "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}

# data3 = {
#             "category": "양서파충류",
#             "createdAt": "2023-11-03 00:24:33",
#             "hangang_alphabet": "R",
#             "imgLink": "gs://hanganggo-88a45.appspot.com/Takydromus_wolteri.jpeg",
#             "lat": 37.56624727206846,
#             "lng": 126.89434875328772,
#             "remark": "우점",
#             "speciesName": "줄장지뱀",
#             "updatedAt": "2023-11-03 00:24:33"
#         }
# species_map.update(data3)
