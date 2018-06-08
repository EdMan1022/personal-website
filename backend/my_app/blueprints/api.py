from flask import Blueprint
from flask_restful import Api

from backend.my_app.models import model_classes
from backend.my_app.helpers.base_resource import BaseResource

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)


for model in model_classes:
    resource_name = "{}Resource".format(model.__name__)
    type(
        resource_name,
        (BaseResource,),
        {
            "class_schema": model.__marshmallow__,
            "out_schema": model.__out_marshmallow__,
            "class_model": model
        }
    )

for resource in BaseResource.__subclasses__():
    api.add_resource(resource, resource.get_url())
