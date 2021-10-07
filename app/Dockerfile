FROM python:3.8-slim AS build-env
# metadata
LABEL dockerfile.version="2"
LABEL software="DevOps-test-app"
LABEL software.version="1"
LABEL maintainer="Martynas J."

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

FROM build-env
EXPOSE 5000
WORKDIR '/app'
COPY . /app
CMD ["python3", "app.py"]