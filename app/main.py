#!/usr/bin/env python3
from flask import Flask
import requests

import config
from metrics.metrics import render_metrics

app = Flask(__name__)


@app.route('/metrics')
def metrics():
    alive_metrics = {}
    try:
        for k, v in config.base_urls.items():
            alive_metrics[f'{k}_api_alive'] = get_alive_metric(v, 'api/v1')
            alive_metrics[f'{k}_reporting_api_alive'] = get_alive_metric(v, 'reports/api/v1')

        return render_metrics(alive_metrics)
    except Exception as e:
        return e.__class__


def get_alive_metric(base_url, api_route):
    result = 0
    try:
        if requests.get(f'https://{base_url}/{api_route}').status_code == 200:
            result = 1
    except Exception as e:
        print(e)
        result = 0

    return result

