import pytest
from selenium import webdriver
from utils import utils

@pytest.fixture(scope="class")
def test_setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(utils.URL)
    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()
