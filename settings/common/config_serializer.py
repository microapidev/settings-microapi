import json


def serialize(config):
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
