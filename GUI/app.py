import gradio as gr
import requests
from PIL import Image
import numpy as np
import io

def predict_digit(image):
    img = Image.fromarray((image * 255).astype(np.uint8))
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    buffered.seek(0)
    
    response = requests.post(
        "http://modelo:5000/predict", 
        files={"file": buffered}
    )
    
    result = response.json()
    
    prediction_type = result.get("prediction", "Unknown")
    prediction_value = result.get("value", "Unknown")
    return f"Predicción: {prediction_type} ({prediction_value})"

iface = gr.Interface(
    fn=predict_digit,
    inputs="sketchpad",
    outputs="text",
    live=False,
    title="Dibuja un número o letra",
    description="Dibuja un número o letra y obtén una predicción."
)

iface.launch(server_name="0.0.0.0", server_port=7860)
