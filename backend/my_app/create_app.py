from flask import Flask
from flask_cors import CORS


def create_app(db, ma, config, blueprints, migrate=None):

    app = Flask(__name__)

    app.config.from_object(config)

    # Configure flask to work with the separate front end Node app
    cors = CORS(app, resources={r"api/*": {"origins": "*"}})

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    db.init_app(app)

    ma.init_app(app)

    if migrate:
        migrate.init_app(app, db)

    return app
