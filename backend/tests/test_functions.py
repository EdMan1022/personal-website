from unittest.mock import MagicMock

from flask import Flask

from .custom_test_base import BaseTestClass
from backend.my_app.create_app import create_app
from backend.my_app.schema.schema_factory import setup_schema
from backend.my_app.models.page import Page
from backend.my_app import db, ma


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
