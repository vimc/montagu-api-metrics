#!/usr/bin/env python3
from flask import Flask
import requests

from metrics.metrics import render_metrics

app = Flask(__name__)

API_HOST =  'montagu_api_1'
API_PORT = 8080
REPORTING_API_HOST = 'montagu_reporting_api_1'
REPORTING_API_PORT = 8081


@app.route('/metrics')
def metrics():
    alive_metrics = {
         'montagu_api_alive': get_alive_metric(API_HOST, API_PORT),
         'montagu_reporting_api_alive': get_alive_metric(REPORTING_API_HOST, REPORTING_API_PORT)
     }

    return render_metrics(alive_metrics)


def get_alive_metric(host, port):
    result = 0
    try:
        if requests.get(f'http://{host}:{port}').status_code == 200:
            result = 1
    except Exception as e:
        print(e)
        result = 0

    return result

