from settings.users import get_user_session
from settings.models import Config


def delete(user_id, api_name):
    tag = "_".join([str(user_id), api_name])
    session = get_user_session(user_id)
    config = session.query(Config).filter_by(config_tag=tag).first()
    if config is None:
        resp = {
            "status": "Failure",
            "message": "Config for {} not found".format(api_name)
        }
        session.close()
        return resp, 404

    try:
        name = config.api_name
        session.delete(config)
        session.commit()

        resp = {
            "status": "Success",
            "message": "Config for '{}' successfully deleted".format(name),
            "result": ""
        }
        session.close()
        return resp, 200

    except Exception as e:
        print(e)
        resp = {
            "status": "Failure",
            "message": "Unexpected Error Occurred"
        }
        session.close()
        return resp, 400
