import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service("\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=s)
    return driver
