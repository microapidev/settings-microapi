from flask import request, url_for


def get():
    url_root = request.url_root
    url_root = url_root[:-1] if url_root[-1] == '/' else url_root
    api_info = {
        "title": "Settings MicroApi",
        "description": "Finally a place to store and dynamically retrieve configurations for your countless apps and services",
        "icon": url_root + url_for('static', filename='img/favicon.ico'),
    }
    return api_info

