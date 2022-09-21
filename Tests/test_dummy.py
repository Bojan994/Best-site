import time
import pytest


@pytest.mark.usefixtures("init_driver")
class TestDummy():
    def test_dummy_function(self):
        self.driver.get("https://www.youtube.com/")
