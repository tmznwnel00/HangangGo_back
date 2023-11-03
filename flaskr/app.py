from flask import Flask, request
from firebase_admin import storage
from flaskr.db import bucket, species_map, collection
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from SpeciesClassification import classify_images

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, My First Flask!"


@app.route("/api/images", methods=["POST"])
def upload_image():
    # save image in firestore, and call function for classify speicies
    image = request.files["image"]
    _, image_extension = os.path.splitext(image.filename)
    current_time = datetime.timestamp(datetime.now())
    image.save(os.path.join(os.getcwd() + "/../images", f"user1_{current_time}{image_extension}"))
    image_path = os.getcwd() + "/../images/" + f"user1_{current_time}{image_extension}"
    
    result = classify_from_image(image_path)
    
    
    collection_data = {
            "user_id": 1,
            "category": "식물",
            "korean_name": result["name"],
            "imgLink": "gs://hanganggo-88a45.appspot.com/Corydalis_incisa_pers.jpeg",
            "remark": "기후변화 생물지표종",
            "lat": 25,
            "lng": 126,
            "hangang_alphabet": "Q",
            "description": "기후변화 생물지표종으로 긴 타원형의 뿌리에서 여러 대의 줄기가 나와 20-50cm까지 자란다. 잎은 3-8cm로 길고 작은 잎이 3장씩 2번 갈라져 나온다. 그늘지고 축축한 땅에서 자라고 5월에 홍자색 꽃을 피우고 4-12cm까지 자란다.",
            "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    print(result)

    imageBlob = bucket.blob("/")
    imageBlob = bucket.blob(result["name"])
    imageBlob.upload_from_filename(image_path)
    
    return "Hello, My First Flask!"


def classify_from_image(image_path):
    result = classify_images.run_model(image_path)
    print(result)

    if float(result[0][3]) < 0.6:
        data = {"name": "Can not classify"}
    else:
        # should convert common name to korean name
        data = {"name": result[0][2]}

    return data


@app.route("/api/maps", methods=["GET"])
def get_species_map():
    query = species_map.get()
    val = query.values()
    result = []
    for specie in val:
        if "hangang_alphabet" not in specie:
            continue
        if "imgLink" not in specie:
            continue
        if specie["hangang_alphabet"] in ["S", "R", "Q", "P", "O", "N", "M2", "M1"]:
            result.append(specie)

    data = {"species": result}

    return data


@app.route("/api/collections", methods=["GET"])
def get_user_collection():
    user = request.args.get("user_id")
    query = collection.order_by_child("user_id").equal_to("1")
    result = query.get()
    return result
