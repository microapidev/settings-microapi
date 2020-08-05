from settings.users import get_user_session
from settings.models import Config


def get(user_id, api_name):
    tag = "_".join([str(user_id), api_name])
    session = get_user_session(user_id)
    config = session.query(Config).filter_by(config_tag=tag).first()
    if config is None:
        resp = {
            "status": "Failure",
            "message": f"Config for {api_name} not found"
        }
        session.close()
        return resp, 404

    try:
        single_config = config.current_config
        resp = {
            "status": "Success",
            "message": f"Config for {api_name}",
            "result": single_config
        }
        session.close()
        return resp, 200

    except Exception as e:
        resp = {
            "status": "Failure",
            "message": "Unexpected Error Occurred"
        }
        session.close()
        return resp, 400
