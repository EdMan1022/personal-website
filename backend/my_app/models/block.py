from backend.my_app.extensions import db


class Block(db.Model):
    """
    Represents content blocks on a website page

    :Inherited Columns:
    id: int pk
    created: datetime
    last_updated: datetime
    """
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    last_updated = db.Column(db.DateTime)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'))
    content = db.Column(db.String)

    __marshmallow__ = None
