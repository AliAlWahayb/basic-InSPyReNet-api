from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
import base64
from transparent_background import Remover

app = Flask(__name__)

# Load model
remover = Remover(resize='dynamic')  # Initialize the background remover

@app.route('/', methods=['POST'])
def process_image():
    data = request.json
    image_data = base64.b64decode(data['image'])

    # Process the image
    img = Image.open(BytesIO(image_data)).convert('RGB')
    out = remover.process(img)  # Process image to add transparent background

    # Convert processed image to base64
    buffered = BytesIO()
    out.save(buffered, format="PNG")
    processed_image_data = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return jsonify({'processed_image': processed_image_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)