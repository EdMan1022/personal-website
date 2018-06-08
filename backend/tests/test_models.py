from unittest.mock import MagicMock

from .custom_test_base import BaseTestClass
from backend.my_app.models import (
    Page, Block
)


class ModelTestBase(BaseTestClass):
    model = None

    def setUp(self):
        super(ModelTestBase, self).setUp()
        self.db_patch = self.create_patch("db")

    def model_init(self):
        """
        Ensures that the test class's model can be instantiated

        This acts as a check against import issues or relationship definition
        issues for the model

        Called by actual test functions in subclasses using Super,
        to prevent this from being run as a test
        :return:
        """
        self.model(**self.base_model_args)


class TestPageModel(ModelTestBase):

    target_path = "backend.my_app.models.page"
    model = Page

    def test_page_init(self):
        super(TestPageModel, self).model_init()


class TestBlockModel(ModelTestBase):

    target_path = "backend.my_app.models.block"
    model = Block

    def setUp(self):
        super(TestBlockModel, self).setUp()
        self.db_patch = self.create_patch("db")

    def test_block_init(self):
        super(TestBlockModel, self).model_init()

