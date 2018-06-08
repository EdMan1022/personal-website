from flask_script import Manager
from flask_migrate import MigrateCommand

from backend.my_app import create_app, db, ma, DevConfig, migrate
from backend.my_app.blueprints import api_blueprint


app = create_app(db, ma, DevConfig(), [api_blueprint],
                 migrate)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':

    # Create any tables for new models
    with app.app_context():
        db.create_all()

    manager.run()
