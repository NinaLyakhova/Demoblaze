import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from Config.Actions import SeleniumAction
from test_demoblaze.data import data_web_address
import os


@pytest.fixture
def browser():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    gecko_path = os.path.join(current_dir, "geckodriver.exe")
    web_service = Service(gecko_path)
    driver = webdriver.Firefox(service=web_service)
    driver.get(data_web_address)
    yield driver
    driver.quit()


@pytest.fixture
def selenium_action(browser):
    selenium_action = SeleniumAction(browser)
    yield selenium_action
