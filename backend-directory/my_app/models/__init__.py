from .page import Page
from .block import Block

from my_app import db, ma
from my_app.schema import setup_schemas
from my_app.schema.block_schema import BlockSchema
from my_app.schema.page_schema import PageOutSchema


# Create a list of the models in the app
model_classes = [Page, Block]

# Bind schema to Models that need it
Block.__marshmallow__ = BlockSchema
Page.__out_marshmallow__ = PageOutSchema


# Run the default schema setup function on the models
setup_schemas(db, ma, model_classes)
