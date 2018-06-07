from flask_script import Manager
from flask_migrate import MigrateCommand

from backend.my_app import create_app, db, ma, DevConfig, migrate


app = create_app(db, ma, DevConfig(), [],
                 migrate)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':

    # Create any tables for new models
    with app.app_context():
        db.create_all()

    manager.run()
