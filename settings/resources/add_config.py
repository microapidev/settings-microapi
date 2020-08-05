from flask import json
from sqlalchemy.exc import IntegrityError
from settings.models import db, Config, config_schema


def post(data):
    try:
        for key in data:
            if key in ["current_config", "previous_config", "default_config"]:
                data[key] = json.dumps(data[key])
        data["config_tag"] = "{}_{}".format(data['user_id'], data['api_name'])

        config = Config(**data)
        db.session.add(config)
        db.session.commit()
        resp = {
            "status": "Success",
            "message": "Create Success",
            "result": config_schema.dump(config)
        }
        return resp, 201

    except IntegrityError:
        resp = {
            "status": "Failure",
            "message": "Config already exists! Please update instead",
            "result": ''
        }
        return resp, 403

    except Exception as e:
        print(e)
        resp = {
            "status": "Failure",
            "message": "Something went wrong",
            "result": ''
        }
        return resp, 400
