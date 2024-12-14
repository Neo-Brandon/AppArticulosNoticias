# Obtener imagen de la misma plataforma para tener exactamente lo mismo
# independientemente del sistema en el que trabajemos
FROM --platform=linux/amd64 python:3.10.4-slim-bullseye

# Variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /code

# Instalar dependencias
COPY ./requerimientos.txt .
RUN pip install -r requerimientos.txt

# Copiar el proyecto
COPY . .