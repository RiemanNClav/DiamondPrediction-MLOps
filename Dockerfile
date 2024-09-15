# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

# Actualiza e instala AWS CLI
RUN apt update -y && apt install awscli -y

# Establece el directorio de trabajo
WORKDIR /app

# Copia el contenido de la aplicación al contenedor
COPY . /app

# Actualiza paquetes y instala las dependencias
RUN apt-get update && pip install -r requirements.txt

# Actualiza scikit-learn a la versión 1.5.2
RUN pip install scikit-learn==1.5.2

# Comando para ejecutar gunicorn con un timeout más alto (120 segundos)
CMD ["gunicorn", "--bind", "0.0.0.0:80", "--timeout", "120", "app:app"]