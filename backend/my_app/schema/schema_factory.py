
def setup_schema(db, ma, this_model):
    """
    Binds a default Marshmallow Schema to a model as an attribute

    :param db: (SQLAlchemy) Declarative base
    :param ma: Flask Marshmallow instance
    :param this_model: The model being modified
    :return: None
    """

    class Meta(object):
        model = this_model
        sqla_session = db.session

    schema_class_name = "{}Schema".format(this_model.__name__)

    schema_class = type(
        schema_class_name,
        (ma.ModelSchema,),
        {'Meta': Meta}
    )

    this_model.__marshmallow__ = schema_class


def setup_schemas(db, ma, models):
    """
    Binds default Marshmallow Schemas to

    :param db:
    :param ma:
    :param models:
    :return:
    """

    for model in models:

        try:
            model.__marshmallow__
        except AttributeError:
            setup_schema(db, ma, model)

        try:
            model.__out_marshmallow__
        except AttributeError:
            model.__out_marshmallow__ = model.__marshmallow__
