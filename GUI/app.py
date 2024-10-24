import gradio as gr
import requests
from PIL import Image
import numpy as np
import io

# Función que se conecta al backend y obtiene la predicción
def predict_digit(image):
    # Convertir la imagen en formato PNG
    img = Image.fromarray((image * 255).astype(np.uint8))
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    buffered.seek(0)
    
    # Enviar la imagen al backend
    response = requests.post(
        "http://modelo:5000/predict", 
        files={"file": buffered}
    )
    
    # Extraer el JSON de la respuesta
    result = response.json()
    
    # Mostrar la predicción en la interfaz
    prediction_type = result.get("prediction", "Unknown")
    prediction_value = result.get("value", "Unknown")
    return f"Predicción: {prediction_type} ({prediction_value})"

# Crear la interfaz gráfica de Gradio
iface = gr.Interface(
    fn=predict_digit,           # Función que se llama al enviar la imagen
    inputs="sketchpad",         # La entrada será el cuadro de dibujo
    outputs="text",             # La salida será texto que muestra la predicción
    live=False,                 # No es necesario hacer predicciones en vivo
    title="Dibuja un número o letra",
    description="Dibuja un número o letra y obtén una predicción."
)

iface.launch(server_name="0.0.0.0", server_port=7860)
