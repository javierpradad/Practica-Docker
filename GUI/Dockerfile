# Usar una imagen base de Python
FROM python:3.9-slim

# Crear un directorio para la aplicación
WORKDIR /ui

# Copiar el código a la imagen
COPY . /ui

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto que utilizará el servicio de Gradio
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]