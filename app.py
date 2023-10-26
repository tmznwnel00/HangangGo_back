from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, My First Flask!'


@app.route('/api/images', methods=['POST'])
def upload_image():
    # save image in firestore, and call function for classify speicies
    image = request.files['image']
    print(image)
    
    return 'Hello, My First Flask!'

def classify_from_image(image):
    
    return 'Hello, My First Flask!'