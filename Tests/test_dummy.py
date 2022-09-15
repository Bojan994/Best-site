import time
import pytest

@pytest.mark.usefixtures("init_driver")
class TestDummy ():
    def test_dummy_function(self):
        print("I am dummy")
        self.driver.get ("http://supersqa.com")