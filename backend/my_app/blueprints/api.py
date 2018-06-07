from flask import request, Blueprint
from flask_restful import Resource, abort, Api
from inflection import underscore

from backend.my_app import db
from backend.my_app.models import model_classes

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)


class BaseResource(Resource):
    class_model = None
    class_schema = None
    url = None

    @classmethod
    def get_url(cls):
        if cls.url:
            return cls.url
        return '/api/{}'.format(underscore(cls.__name__).replace('_resource',
                                                                 ''))

    def get(self):
        schema_instance = self.class_schema()
        get_obj = self.class_model.query.get(request.args['id'])

        if get_obj:
            return schema_instance.dump(get_obj)
        else:
            return abort(404, message="No {} object found with id {}".format(
                self.class_model.__name__, request.args['id']
            ))

    def post(self):
        schema_instance = self.class_schema()
        result = schema_instance.load(request.json, db.session)
        post_obj = result.data
        db.session.add(post_obj)
        db.session.commit()
        return schema_instance.dump(post_obj)

    def put(self):
        schema_instance = self.class_schema()
        result = schema_instance.load(request.json, db.session)
        put_obj = result.data
        db.session.commit()
        return schema_instance.dump(put_obj)

    def delete(self):
        schema_instance = self.class_schema()
        result = schema_instance.load(request.json, db.session)
        delete_obj = result.data
        db.session.delete(delete_obj)
        db.session.commit()
        return schema_instance.dump(delete_obj)


for model in model_classes:
    resource_name = "{}Resource".format(model.__name__)
    type(
        resource_name,
        (BaseResource,),
        {
            "class_schema": model.__marshmallow__,
            "class_model": model
        }
    )

for resource in BaseResource.__subclasses__():
    api.add_resource(resource, resource.get_url())
