#!/usr/bin/env python3

"""This application is purely made for learning purposes"""

import os
from flask import Flask, render_template, request, redirect
import redis

# Try to read application parameters from environment
try:
    REDIS_HOST = os.environ['REDIS_HOST']
except LookupError:
    REDIS_HOST = "localhost"

# REDIS_PORT = os.environ['REDIS_PORT']
try:
    REDIS_PORT = os.environ['REDIS_PORT']
except LookupError:
    REDIS_PORT = 6379

try:
    BIND_ADDR = os.environ['BIND_ADDR']
except LookupError:
    BIND_ADDR = '0.0.0.0'

try:
    BIND_PORT = os.environ['BIND_PORT']
except LookupError:
    BIND_PORT = 5000

# Create redis connection and initialize flask
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
app = Flask(__name__)

# Render main page
@app.route('/', methods=['GET'])
def render_page():
    # Get all keys from redis
    key_array = r.keys("*")
    decoded_keys = []
    decoded_values =[]
    # For every key from redis
    for x in key_array:
        # Convert key from binary data to text
        tmp = x.decode("utf-8")
        # Append key to list
        decoded_keys.append(tmp)
        # Convert current keys value to text and append it to a list
        decoded_values.append(r.get(tmp).decode("utf-8"))
    # Form a dictionary with key:value pairs
    results = {decoded_keys[i]: decoded_values[i] for i in range(len(decoded_keys))}
    # Render template with results
    return render_template('index.html', res=results)

# Function for adding new key:value pair to redis
@app.route('/add', methods=['GET'])
def add_value():
    # Get key and value from request URL arguments
    key = request.args.get('key')
    value = request.args.get('value')
    # Add key:value to redis
    r.mset({key: value})
    # Redirect to main page to show results
    return redirect(f"/")

# Run flask application
app.run(host=BIND_ADDR, port=BIND_PORT)
