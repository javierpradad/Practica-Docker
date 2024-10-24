from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf  # Asumiendo que usas un modelo con TensorFlow o Keras
from PIL import Image
import io

app = Flask(__name__)

# Cargar el modelo preentrenado para predecir letras o números
model = tf.keras.models.load_model('model.h5')
print("-------------modelo cargado----------------")

@app.route('/predict', methods=['POST'])
def predict():
    print("-------------mensaje recibido----------------")
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    img = Image.open(io.BytesIO(file.read())).convert('L')
    print("-------------imagen abierta----------------")
    img = img.resize((28, 28))  # Redimensiona si es necesario
    img = np.array(img) / 255.0  # Normaliza los píxeles
    img = img.reshape(1, 28, 28, 1)  # Ajustar forma para el modelo
    print("-------------imagen transformada----------------")

    
    prediction = model.predict(img)
    label = np.argmax(prediction, axis=1)
    print("-------------predicción hecha----------------")

    
    if label[0] < 10:
        result = {'prediction': 'number', 'value': str(label[0])}
    else:
        result = {'prediction': 'letter', 'value': chr(label[0] + 55)}  # Suponiendo A-Z
    
    print("-------------mensaje devuelto----------------")

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
