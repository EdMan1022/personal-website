from marshmallow import fields

from my_app.extensions import ma
from my_app.models.page import Page

from .block_schema import BlockSchema


class PageOutSchema(ma.ModelSchema):
    """
    Schema class for GET routes of the Page model

    Overrides the Block relationship so that it returns the data instead of pk
    """

    block = fields.Nested(BlockSchema, many=True, exclude=('page', ))

    class Meta:
        model = Page
