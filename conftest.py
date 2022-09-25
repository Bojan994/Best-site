import pytest
from selenium import webdriver
import os



@pytest.fixture(scope="class")
def init_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()
