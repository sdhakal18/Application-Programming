from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from config import Config
from extensions import db, jwt
from models.user import User
from resources.user import UserListResource, UserResource, MeResource
from resources.token import TokenResource
from resources.schedule import ScheduleListResource, ScheduleResource, SchedulePublishResource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.app_context().push()

    register_extensions(app)
    register_resources(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    api = Api(app)

    api.add_resource(ScheduleListResource, '/schedules')
    api.add_resource(ScheduleResource, '/schedules/<int:schedule_id>')
    api.add_resource(SchedulePublishResource, '/schedules/<int:schedule_id>/publish')
    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<string:username>')
    api.add_resource(TokenResource, '/token')
    api.add_resource(MeResource, '/me')


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)



