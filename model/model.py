from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from PIL import Image
import io

app = Flask(__name__)

model = tf.keras.models.load_model('model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No se ha recibido la imagen'}), 400
    
    file = request.files['file']
    img = Image.open(io.BytesIO(file.read())).convert('L')
    img = img.resize((28, 28)) 
    img = np.array(img) / 255.0
    img = img.reshape(1, 28, 28, 1) 

    prediction = model.predict(img)
    label = np.argmax(prediction, axis=1)
    
    if label[0] < 10:
        result = {'prediccion': 'number', 'value': str(label[0])}
    else:
        result = {'prediccion': 'letter', 'value': chr(label[0] + 55)}

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
