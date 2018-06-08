from .page import Page
from .block import Block

from backend.my_app import db, ma
from backend.my_app.schema import setup_schemas

# Create a list of the models in the app
model_classes = [Page, Block]

# Run the default schema setup function on the models
setup_schemas(db, ma, model_classes)
