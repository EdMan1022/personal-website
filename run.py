from backend.my_app import create_app, DevConfig, ma, db
from backend.my_app.blueprints import api_blueprint


app = create_app(db=db, ma=ma, config=DevConfig(),
                 blueprints=[api_blueprint],)

if __name__ == '__main__':
    app.run()
