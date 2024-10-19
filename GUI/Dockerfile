# Usar una imagen base de Python
FROM python:3.9-slim

# Crear un directorio para la aplicación
WORKDIR /gui

# Copiar el código a la imagen
COPY . /gui

# Instalar las dependencias
RUN pip install -r requirments.txt

# Exponer el puerto que utilizará el servicio de Gradio
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]