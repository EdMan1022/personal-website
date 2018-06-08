from .custom_test_base import BaseTestClass
from backend.my_app.models.page import Page


class TestPageModel(BaseTestClass):

    target_path = "backend.my_app.models.page"

    def setUp(self):
        self.db_patch = self.create_patch("db")

    def test_page_init(self):

        page = Page()


