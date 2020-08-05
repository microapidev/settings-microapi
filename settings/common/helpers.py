import requests
from flask import request
from settings.config import DASHBOARD_API_SETTINGS_ROUTE, LOCAL_TEST_DB_URI


def serialize_config(config):
    json_config = {
        "id": config.id,
        "user_id": config.user_id,
        "api_name": config.api_name,
        "config_tag": config.config_tag,
        "current_config": config.current_config,
        "previous_config": config.previous_config,
        "default_config": config.default_config,
        "created_at": config.created_at,
        "updated_at": config.updated_at,
    }
    return json_config


# todo: this function should query the db to check authorization and get settings (like db uri)
def get_api_settings(user_id):
    url_root = request.url_root[:-1] if request.url_root[-1] == '/' else request.url_root
    url = url_root + DASHBOARD_API_SETTINGS_ROUTE
    params = {
        'user_id': user_id,
    }

    req = requests.request('GET', url=url, params=params)
    if req.status_code != 200:
        error_text = 'ERROR: Unable to get settings from dashboard'
        print(error_text, '\n', req.reason)
        return error_text, req.status_code

    req = req.json()
    return req, 200


def get_db_url(user_id):
    user_settings, status = get_api_settings(user_id)
    if status == 200:
        for setting in user_settings:
            if setting['setting_key'] == 'database_url':
                return setting['setting_value']
    # todo: reverse comment of this section when route is available on dashboard
    # return ''
    return LOCAL_TEST_DB_URI.format(user_id)
