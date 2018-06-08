from backend.my_app.extensions import ma
from backend.my_app.models.block import Block


class BlockSchema(ma.ModelSchema):

    class Meta:
        model = Block
