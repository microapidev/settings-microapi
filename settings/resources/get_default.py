
from settings.models import Config


def get(user_id, api_name):
    tag = "_".join([str(user_id), api_name])
    config = Config.query.filter_by(config_tag=tag).first()

    if config is None:
        resp = {
            "status": "Failure",
            "message": "No Config found for {} API".format(api_name)
        }

        return resp, 404

    default_config = getattr(config, "default_config", None)

    if default_config == "{}":
        resp = {
            "status": "Failure",
            "message": "No default config defined for {} API".format(api_name)
        }

        return resp, 404

    resp = {
        "status": "Success",
        "message": "Default config retrieve success",
        "result": default_config
    }

    return resp, 200
