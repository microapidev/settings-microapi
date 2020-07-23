from settings.models import Config, config_schema
from settings.config import db


def post(data):
    tag = "_".join([str(data["user_id"]), data["api_name"]])
    config = Config.query.filter_by(config_tag=tag).first()
    if config is None:
        resp = {
            "status": "Failure",
            "message": "Config for {} not found".format(data["api_name"])
        }

        return resp, 404

    try:
        for name in ["current_config", "default_config"]:
            if name in data.keys():
                for k in data[name].keys():
                    # __setattr__(key, value) if value is none
                    # use the existing value.
                    config.__setattr__(
                        k, data[name].get(k, config.__getattr__(k)))
    except Exception as e:
        print(e)
        resp = {
            "status": "Failure",
            "message": "Unexpected Error Occurred"
        }

        return resp, 400

    db.session.add(config)
    db.session.commit()

    resp = {
        "status": "Success",
        "message": "Update Success",
        "result": config_schema.dump(config)
    }

    return resp, 200
