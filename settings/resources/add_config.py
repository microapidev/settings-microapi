from flask import json
from sqlalchemy.exc import IntegrityError
from settings.models import Config, config_schema
from settings.common.users import get_user_session
# from settings.common.config_serializer import serialize


def post(data):
    try:
        for key in data:
            if key in ["current_config", "previous_config", "default_config"]:
                data[key] = json.dumps(data[key])
        data["config_tag"] = "{}_{}".format(data['user_id'], data['api_name'])

        config = Config(**data)
        session = get_user_session(data['user_id'])
        session.add(config)
        session.commit()

        json_config = config_schema.dump(config)
        session.close()
        resp = {
            "status": "Success",
            "message": "Create Success",
            "result": json_config
        }
        return resp, 201

    except IntegrityError as e:
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
