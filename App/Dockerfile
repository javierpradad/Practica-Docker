# Usar una imagen base de TensorFlow
FROM tensorflow/tensorflow:2.10.0

# Crear un directorio para la aplicación
WORKDIR /app

# Copiar el código a la imagen
COPY . /app

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto que utilizará el servicio
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "model.py"]