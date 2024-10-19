import gradio as gr
import requests
from PIL import Image

# Función que interactúa con el contenedor de inferencia
def classify_image(image):
    img_bytes = image.tobytes()
    # Enviar la imagen al servicio de inferencia
    response = requests.post('http://inference:5000/predict', files={'image': img_bytes})
    predictions = response.json()

    # Formatear las predicciones para mostrarlas en la interfaz
    result = {pred["label"]: pred["probability"] for pred in predictions}
    return result

# Crear la interfaz de Gradio
iface = gr.Interface(fn=classify_image, 
                     inputs=gr.Image(type="pil"),
                     outputs=gr.Label(num_top_classes=3),
                     title="Image Classification with MobileNetV2",
                     description="Sube una imagen para clasificarla usando MobileNetV2")

# Ejecutar la interfaz
if __name__ == '__main__':
    iface.launch(server_name="0.0.0.0", server_port=8080)