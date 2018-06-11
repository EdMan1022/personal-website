from flask import Blueprint
from flask_restful import Api, abort

from my_app.models import model_classes, Page
from my_app.helpers.base_resource import BaseResource

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


class PagesResource(BaseResource):
    """
    Special resource to handle gets of all pages

    """
    class_model = Page
    class_schema = Page.__marshmallow__
    out_schema = Page.__out_marshmallow__
    url = '/api/pages/'

    message = "Method not allowed"

    def get(self):
        schema_instance = self.out_schema(many=True)

        objs = self.class_model.query.all()
        result = schema_instance.dump(objs)
        return result.data

    def post(self):
        return abort(405, message=self.message)

    def put(self):
        return abort(405, message=self.message)

    def delete(self):
        return abort(405, message=self.message)


for resource in BaseResource.__subclasses__():
    api.add_resource(resource, resource.get_url())



