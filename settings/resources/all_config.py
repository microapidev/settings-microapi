from settings.models import Config, config_schema_many


def get(user_id):
    config = Config.query.filter_by(user_id=user_id).all()
    if config != []:
        resp = {
            "status": "Success",
            "message": f"All configuration associated with user {user_id}",
            "result": config_schema_many.dump(config)
        }
        return resp, 200
    resp = {
        "status": "Failure",
        "message": "Invalid Id",
        "result": ''
    }
    return resp, 404
