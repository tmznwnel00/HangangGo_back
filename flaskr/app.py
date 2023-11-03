from flask import Flask, request
from firebase_admin import storage
from flaskr.db import bucket, species_map, collection
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# from SpeciesClassification import classify_images

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, My First Flask!'


@app.route('/api/images', methods=['POST'])
def upload_image():
    # save image in firestore, and call function for classify speicies
    image = request.files["image"]
    _, image_extension = os.path.splitext(image.filename)

    image.save(os.path.join(os.getcwd() + '/../images', f'user1_2{image_extension}'))
    image_path = os.getcwd() + '/../images/' + f'user1_2{image_extension}'
    classify_from_image(image_path)
    
    return 'Hello, My First Flask!'

def classify_from_image(image_path):

    result = classify_images.run_model(image_path)
    print(result)
    
    data = {
        "result" : result[0][2]
    }
    
    return data

@app.route('/api/maps', methods=['GET'])
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

    data = {
        "species" : result
    }
    
    return data

@app.route('/api/collections', methods=['GET'])
def get_user_collection():
    user = request.args.get("user_id")
    query = collection.order_by_child('user_id').equal_to("1")
    result = query.get()
    return result