import requests
from flask import request, url_for
from settings.config import SWAGGER_V2_URL, OPEN_API_CONVERTER_URL


def get_info():
    url_root = request.url_root
    url_root = url_root[:-1] if url_root[-1] == '/' else url_root
    api_info = {
        "title": "Settings MicroApi",
        "description": "Finally a place to store and dynamically retrieve configurations "
                       "for your countless apps and services",
        "icon": url_root + url_for('static', filename='img/favicon.ico'),
    }
    return {'message': 'API info retrieved successfully', 'data': api_info, 'success': True}, 200


def get_docs():
    url_root = request.url_root
    url_root = url_root[:-1] if url_root[-1] == '/' else url_root

    req = requests.request('GET', url=OPEN_API_CONVERTER_URL, params={'url': url_root + SWAGGER_V2_URL})
    if req.status_code != 200:
        return {'message': 'Something went wrong', 'status': 'Failure'}, req.status_code

    return {'message': 'API docs retrieve successfully',
            'data': req.json(),
            'success': True}, 200

