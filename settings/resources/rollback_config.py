from settings.models import db, Config, config_schema


def rollback(user_id, api_name):
    tag = "_".join([str(user_id), api_name])
    config = Config.query.filter_by(config_tag=tag).first()
    if config is None:
        resp = {
            "status": "Failure",
            "message": "No configuration found for {} API".format(api_name)
        }

        return resp, 404

    try:
        current = getattr(config, "current_config", None)
        previous = getattr(config, "previous_config", None)
        default = getattr(config, "default_config", None)

        if previous:
            config.current_config = previous
            config.previous_config = current
        else:
            if default:
                config.current_config = default
                config.previous_config = current
            else:
                resp = {
                    "status": "Failure",
                    "message": "No previous or default config to rollback"
                }

                return resp, 400
        db.session.add(config)
        db.session.commit()
    except Exception as e:
        print(e)
        resp = {
            "status": "Error",
            "message": "Unexpected Error Occurred"
        }

        return resp, 403

    resp = {
        "status": "Success",
        "message": "Config rollback Success",
        "result": config_schema.dump(config)["current_config"]
    }

    return resp, 200
