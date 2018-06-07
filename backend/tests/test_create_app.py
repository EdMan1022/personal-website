from unittest.mock import MagicMock

from flask import Flask

from .custom_test_base import BaseTestClass
from backend.my_app.create_app import create_app


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
