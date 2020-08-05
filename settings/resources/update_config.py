import json
# from settings.common.config_serializer import serialize
from settings.common.users import get_user_session
from settings.models import Config, config_schema


def post(data):
    tag = "_".join([str(data["user_id"]), data["api_name"]])
    session = get_user_session(data['user_id'])
    config = session.query(Config).filter_by(config_tag=tag).first()
    if config is None:
        resp = {
            "status": "Failure",
            "message": "Config for {} not found".format(data["api_name"])
        }

        return resp, 404

    try:
        # before performing the update we set the current
        # config as the previous config so that we can rollback
        current = config.current_config

        for name in ["current_config", "default_config"]:
            if name in data.keys():
                config_var = getattr(config, name)

                if not config_var:
                    config_var = {}
                else:
                    config_var = json.loads(config_var)

                for k in data[name].keys():
                    config_var[k] = data[name].get(k)
                config_var = json.dumps(config_var)
                config.__setattr__(name, config_var)
    except Exception as e:
        print(e)
        resp = {
            "status": "Failure",
            "message": "Unexpected Error Occurred"
        }
        return resp, 400

    config.previous_config = current
    # session = get_user_session(data['user_id'])
    session.add(config)
    session.commit()

    json_config = config_schema.dump(config)
    session.close()

    resp = {
        "status": "Success",
        "message": "Update Success",
        "result": json_config
    }
    return resp, 200
