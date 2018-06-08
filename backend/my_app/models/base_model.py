from backend.my_app.extensions import db


class BaseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    last_updated = db.Column(db.DateTime)
