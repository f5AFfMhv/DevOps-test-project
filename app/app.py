#!/usr/bin/env python3

"""This application is purely made for learning purposes"""

import os
from flask import Flask, render_template, request, redirect
from prometheus_flask_exporter import PrometheusMetrics
import redis

# Try to read application parameters from environment
try:
    REDIS_HOST = os.environ['REDIS_HOST']
except LookupError:
    REDIS_HOST = "localhost"

try:
    REDIS_PORT = os.environ['REDIS_PORT']
except LookupError:
    REDIS_PORT = 6379

try:
    FLASK_ENV = os.environ['FLASK_ENV']
except LookupError:
    FLASK_ENV = "Not set"

try:
    APP_VERS = os.environ['APP_VERS']
except LookupError:
    APP_VERS = "Not set"

# Create redis connection and initialize flask
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/', methods=['GET'])
def render_page():
    """Render main page"""
    # Get all keys from redis
    key_array = r.keys("*")
    decoded_keys = []
    decoded_values =[]
    # For every key from redis
    for key in key_array:
        # Convert key from binary data to text
        tmp = key.decode("utf-8")
        # Append key to list
        decoded_keys.append(tmp)
        # Convert current keys value to text and append it to a list
        decoded_values.append(r.get(tmp).decode("utf-8"))
    # Form a dictionary with key:value pairs
    results = {decoded_keys[idx]: decoded_values[idx] for idx in range(len(decoded_keys))}
    # Render template with results
    return render_template('index.html', res=results, redis_host=REDIS_HOST, redis_port=REDIS_PORT, flask_env=FLASK_ENV, app_vers=APP_VERS)

@app.route('/add', methods=['GET'])
def add_value():
    """Function for adding new key:value pair to redis"""
    # Get key and value from request URL arguments
    key = request.args.get('key')
    value = request.args.get('value')
    # Add key:value to redis
    r.mset({key: value})
    # Redirect to main page to show results
    return redirect("/")

@app.route('/dashboard/flask', methods=['GET'])
def flask_dashboard():
    """Function for redirecting to grafana flask dashboard"""
    # Redirect to flask dashboard
    return redirect("/grafana/d/flask_dashboard/")
