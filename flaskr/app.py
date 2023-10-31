from flask import Flask, request
from firebase_admin import storage
from flaskr.db import bucket, species_map, collection
import sys
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, My First Flask!'


@app.route('/api/images', methods=['POST'])
def upload_image():
    # save image in firestore, and call function for classify speicies
    image = request.files["image"]
    _, image_extension = os.path.splitext(image.filename)

    image.save(os.path.join(os.getcwd() + '/../images', f'user1_1{image_extension}'))
    image_path = os.getcwd() + '/../images/' + f'hi{image_extension}'
    classify_from_image(image_path)
    
    return 'Hello, My First Flask!'

def classify_from_image(image_path):
    sys.argv = [image_path]
    
    with open("../SpeciesClassification/classify_images.py", "r") as classify:
        code = classify.read()
    
    exec(code)
    
    return 'Hello, My First Flask!'

@app.route('/api/maps', methods=['GET'])
def get_species_map():
    return species_map.get()

@app.route('/api/collections', methods=['GET'])
def get_user_collection():
    user = request.args.get("user_id")
    query = collection.order_by_child('user_id').equal_to("1")
    result = query.get()
    return result