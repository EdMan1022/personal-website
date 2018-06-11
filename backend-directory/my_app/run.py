from my_app import create_app, DevConfig, ma, db
from my_app.blueprints import api_blueprint
from os import environ


app = create_app(db=db, ma=ma, config=DevConfig(),
                 blueprints=[api_blueprint],)

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=environ["PORT"])
