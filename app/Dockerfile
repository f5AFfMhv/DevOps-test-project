FROM python:3.8-slim AS build-env
# metadata
LABEL software="DevOps-test-app"
LABEL maintainer="Martynas J."

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

FROM build-env
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV APP_VERS=v1.0.0

EXPOSE 5000
WORKDIR '/app'
COPY . /app
CMD ["flask", "run"]