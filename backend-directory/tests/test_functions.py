from unittest.mock import MagicMock

from flask import Flask

from .custom_test_base import BaseTestClass
from my_app.create_app import create_app
from my_app.schema.schema_factory import setup_schema
from my_app.models.page import Page
from my_app import db, ma
from my_app.helpers.base_resource import BaseResource


class TestCreateApp(BaseTestClass):

    def test_create_with_mocks(self):
        mock_db = MagicMock()
        mock_ma = MagicMock()
        mock_config = MagicMock()
        mock_blueprints = MagicMock()
        mock_migrate = MagicMock()

        app = create_app(mock_db, mock_ma, mock_config, mock_blueprints,
                         mock_migrate)

        self.assertIsInstance(app, Flask)


class TestSchemaFactory(BaseTestClass):
    """
    Tests the function that creates default Marshmallow Schemas for the models
    """

    def setUp(self):
        super(TestSchemaFactory, self).setUp()
        self.mock_db = MagicMock()
        self.mock_ma = MagicMock()
        self.mock_model = MagicMock()
        self.mock_model.__name__ = 'TEST'

    def test_setup_schema(self):
        """
        Test that the setup_schema alters the correct attribute on a model

        :return:
        """
        setup_schema(db, ma, Page)

        self.assertIsNotNone(Page.__marshmallow__)


class TestBaseResource(BaseTestClass):

    target_path = 'my_app.helpers.base_resource'

    def setUp(self):
        super(TestBaseResource, self).setUp()

        self.request_patch = self.create_patch('request')
        self.db_patch = self.create_patch('db')

        # Set up a test resource
        self.base_resource = BaseResource()
        self.base_resource.class_model = MagicMock()
        self.base_resource.class_schema = MagicMock()
        self.base_resource.out_schema = MagicMock()
        self.base_resource.url = 'test'

    def test_resource(self):

        self.base_resource.get()
        self.base_resource.post()
        self.base_resource.put()
        self.base_resource.delete()

