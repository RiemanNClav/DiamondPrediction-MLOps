FROM python:3.8-slim-buster

# Actualiza e instala AWS CLI
RUN apt update -y && apt install awscli -y

# Establece el directorio de trabajo
WORKDIR /app

# Copia el contenido de la aplicación al contenedor
COPY . /app

# Actualiza paquetes e instala las dependencias
RUN apt-get update && pip install -r requirements.txt

# Instala la versión 1.3.2 de scikit-learn compatible con Python 3.8
#new change
RUN pip install scikit-learn==1.3.2

# Comando para ejecutar gunicorn con un timeout más alto (120 segundos)
CMD ["gunicorn", "--bind", "0.0.0.0:80", "--timeout", "120", "app:app"]
