from enum import Enum

from backend.my_app.extensions import db


class PageType(Enum):
    """
    Enumerated type for the different types of pages allowed by the app
    """
    resume = 'resume'
    blog_post = 'blog_post'
    project = 'project'


class Page(db.Model):
    """
    Object relational mapping for table containing pages on a website

    A page has a page type (Resume, blog post, project overview, etc.),
    metadata columns (created date, last modified, etc),
    and relationships to blocks on the page that contain the actual content

    :Inherited Columns:
    id: int pk
    created: datetime
    last_updated: datetime
    """
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    last_updated = db.Column(db.DateTime)
    page_type = db.Column(db.Enum(PageType))
    published = db.Column(db.Boolean)

    block = db.relationship('Block', backref=db.backref('page'))

    __marshmallow__ = None
