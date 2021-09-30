FROM python:3.8-slim AS build-env
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

FROM build-env
EXPOSE 5000
WORKDIR '/app'
COPY . /app
CMD ["python3", "app.py"]