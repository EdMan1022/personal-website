from my_app.extensions import ma
from my_app.models.block import Block


class BlockSchema(ma.ModelSchema):

    class Meta:
        model = Block
