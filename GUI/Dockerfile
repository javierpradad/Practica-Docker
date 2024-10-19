# Usar una imagen base de Python
FROM python:3.9-alpine3.20

# Crear un directorio para la aplicación
WORKDIR /gui

# Copiar el código a la imagen
COPY . /gui

# Instalar las dependencias
RUN pip install -r requirments.txt

EXPOSE 8080
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]