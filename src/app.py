#!/usr/bin/env python

from flask import Flask, jsonify, Request, Response
from yelpapi import YelpApi

import yaml
import os

config = yaml.load(open('config.yml'))

env = os.environ['ENV']
if env is 'DEV':
    debug = True
    SECRET_KEY = 'dev key'
else:
    debug = False

if 'PORT' in os.environ:
    port = os.environ['PORT']
elif 'port' in config['server']:
    port = config['server']['port']
else:
    port = 4000

host = config['server']['host']

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({})

app.run(host=host, port=port, debug=debug)
