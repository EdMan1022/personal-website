from flask_restful import Resource, abort
from inflection import underscore
from flask import request

from backend.my_app import db


class BaseResource(Resource):
    class_model = None
    class_schema = None
    out_schema = None
    url = None

    @classmethod
    def get_url(cls):
        if cls.url:
            return cls.url
        return '/api/{}'.format(underscore(cls.__name__).replace('_resource',
                                                                 ''))

    def get(self):
        schema_instance = self.out_schema()
        get_obj = self.class_model.query.get(request.args['id'])

        if get_obj:
            schema_result = schema_instance.dump(get_obj)
            return schema_result.data
        else:
            return abort(404, message="No {} object found with id {}".format(
                self.class_model.__name__, request.args['id']
            ))

    def post(self):
        schema_instance = self.class_schema()
        out_schema_instance = self.out_schema()

        result = schema_instance.load(request.json, db.session)
        post_obj = result.data
        db.session.add(post_obj)
        db.session.commit()
        schema_result = out_schema_instance.dump(post_obj)
        return schema_result.data

    def put(self):
        schema_instance = self.class_schema()
        out_schema_instance = self.out_schema()

        result = schema_instance.load(request.json, db.session)
        put_obj = result.data
        db.session.commit()
        schema_result = out_schema_instance.dump(put_obj)
        return schema_result.data

    def delete(self):
        schema_instance = self.class_schema()
        out_schema_instance = self.out_schema()

        result = schema_instance.load(request.json, db.session)
        delete_obj = result.data
        db.session.delete(delete_obj)
        db.session.commit()
        schema_result = out_schema_instance.dump(delete_obj)
        return schema_result.data
