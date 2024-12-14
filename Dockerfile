# Obtener imagen de la misma plataforma para tener exactamente lo mismo
# independientemente del sistema en el que trabajemos
FROM --platform=linux/amd64 python:3.10.4-slim-bullseye

# Variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Variables de entorno paypal
ENV PAYPAL_CLIENT_ID=AbtPgwSybv7Qk5j9qC2BSi_SHRRoPQXEpWoHrkUIf9rZfvBJSsuaof7341MPFUuCB7H4PCyaHLvVxmUh
ENV PAYPAL_CLIENT_SECRET=EJoTLyzs9XwdJdtND7FVoDjNczzKKy_8WaWbsUnGvLmgIgJjlWJmnbuv7GBxcaP6S28zgS-WyES9eGaK
ENV PAYPAL_MODE=sandbox


# Directorio de trabajo
WORKDIR /code

# Instalar dependencias
COPY ./requerimientos.txt .
RUN pip install -r requerimientos.txt

# Copiar el proyecto
COPY . .