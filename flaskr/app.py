from flask import Flask, request
from firebase_admin import storage
from flaskr.db import bucket

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, My First Flask!'


@app.route('/api/images', methods=['POST'])
def upload_image():
    # save image in firestore, and call function for classify speicies
    params = request.get_json()
    # image_path = params['iamge_path']
    image_path = 'gs://hanganggo-88a45.appspot.com/sample.webp'
    
    blob = bucket.blob(image_path)
    
    return 'Hello, My First Flask!'

def classify_from_image(image):
    
    return 'Hello, My First Flask!'