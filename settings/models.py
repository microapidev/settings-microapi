from datetime import datetime
from settings.config import db, ma


class Config(db.Model):
    __tablename__ = 'configurations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    api_name = db.Column(db.String(), nullable=False)
    config_tag = db.Column(db.String, nullable=False, unique=True)
    current_config = db.Column(db.String(), nullable=False)
    previous_config = db.Column(db.String(), nullable=True)
    default_config = db.Column(db.String(), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __str__(self):
        return "Config <{id}: {api_name}>".format(id=self.id, api_name=self.api_name)

    __repr__ = __str__


class ConfigSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Config
        sqla_session = db.session

config_schema = ConfigSchema()
config_schema_many = ConfigSchema(many=True)
/config/delete/{user_id}/{api_name}:
    delete:
      tags: ["Configuration"]
      summary: "Delete Configuration"
      description: "Delete Configuration that match configTag"
      operationId: settings.resources.delete_config.delete
      consumes:
        - "application/json"
      produces:
        - "application/json"
      parameters:
        - name: "user_id"
          in: "path"
          description: "User id to delete"
          required: true
          type: "string"
        - name: "api_name"
          in: "path"
          description: "api_name to delete"
          required: true
          type: "string"
      responses:
        "201":
          description: "Configuration Deleted"
          schema:
            $ref: "#/definitions/Config"
        "400":
          description: "Invalid input"
        "404":
          description: "Configuration does not exist"