from flask import Flask, request, jsonify
from firebase_admin import storage
from flaskr.db import bucket, species_map, collection
import sys
import os
from datetime import datetime
import mapping

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
    
    if result["name"] != "Can not classify":
        
        imageBlob = bucket.blob("/")
        imageBlob = bucket.blob(result["name"].replace(" ", "_"))
        imageBlob.upload_from_filename(image_path)
        mapping.mapping_dict[result["name"]]["createdAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mapping.mapping_dict[result["name"]]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mapping.mapping_dict[result["name"]]["user_id"] = 1
        mapping.mapping_dict[result["name"]]["lat"] = 1
        mapping.mapping_dict[result["name"]]["lng"] = 1
        
        data : {
            "res" : mapping.mapping_dict[result["name"]],
            "prob" : result["prob"]
        }
        return jsonify(data)
    
    else:
        data : {
            "res" : result["name"],
            "prob" : result["prob"]
        }
        return jsonify(data)


def classify_from_image(image_path):
    result = classify_images.run_model(image_path)
    print(result)

    if float(result[0][3]) < 0.6:
        data = {
            "name": "Can not classify",
            "prob": result[0][3]
            }
    else:
        # should convert common name to korean name
        data = {
            "name": result[0][2],
            "prob": result[0][3]
            }

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

    return jsonify(data)


@app.route("/api/collections", methods=["GET"])
def get_user_collection():
    user = request.args.get("user_id")
    query = collection.order_by_child("user_id").equal_to(1)
    result = query.get()
    
    return jsonify(result)
