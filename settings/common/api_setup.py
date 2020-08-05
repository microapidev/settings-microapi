# imports go here

api_settings = [
    {
        "setting_name": "Database URL (Served SQLite, PostgreSQL or MySQL)",
        "setting_type": "String",
        "setting_key": "database_url",
        "setting_required": True,
        "setting_value": None
    },

]


def get():
    # do stuff
    return api_settings, 200


def patch(data):
    # do stuff
    pass
