import gradio as gr
import requests

# URL del contenedor 2 (el que realiza la suma)
SUM_SERVER_URL = "http://sum-container:5000/sum"

def send_numbers_and_get_sum(num1, num2):
    data = {'num1': num1, 'num2': num2}
    # Realizamos una petición POST al servidor de suma
    response = requests.post(SUM_SERVER_URL, json=data)
    if response.status_code == 200:
        return response.json().get('sum', 'Error al sumar')
    else:
        return 'Error en el servidor de suma'

# Interfaz gráfica de Gradio
inputs = [gr.Number(label="Número 1"), gr.Number(label="Número 2")]
output = gr.Textbox(label="Resultado de la suma")

gr.Interface(fn=send_numbers_and_get_sum, inputs=inputs, outputs=output).launch(server_name="0.0.0.0")
