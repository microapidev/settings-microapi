from settings.models import Config, config_schema_many
from settings.users import get_user_session


def get(user_id):
    session = get_user_session(user_id)
    config = session.query(Config).all()
    if config:
        resp = {
            "status": "Success",
            "message": f"All configuration associated with user {user_id}",
            "result": config_schema_many.dump(config)
        }
        session.close()
        return resp, 200
    resp = {
        "status": "Failure",
        "message": "Invalid Id",
        "result": ''
    }
    session.close()
    return resp, 404
