import json
from settings.models import Config, config_schema
from settings.config import db


def delete(data):
    tag = "_".join([str(data["user_id"]), data["api_name"]])
    config = Config.query.filter_by(config_tag=tag).first()
    if config is None:
        resp = {
            "status": "Failure",
            "message": "Config for {} not found".format(data["api_name"])
        }

        return resp, 404

    try:
        name = config.api_name
        db.session.delete(config)
        db.session.commit() 

        resp = {
            "status": "Success",
            "message": "Config for '{}' successfully deleted".format(name),
            "result": ""
        }

        return resp, 200
    except Exception as e:
        print(e)
        resp = {
            "status": "Failure",
            "message": "Unexpected Error Occurred"
        }

        return resp, 400
    
