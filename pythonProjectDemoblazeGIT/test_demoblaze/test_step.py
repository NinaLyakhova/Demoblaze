import pytest

from Config.Config import *
from test_demoblaze.locators import *
from test_demoblaze.data import *


@pytest.fixture
def login_form_demoblaze(browser, selenium_action): # pytest -k login test_step.py
    def login_function():
        selenium_action.action_click_element(locator_button_login_1)
        selenium_action.action_fill_input(locator_field_user_name, data_user_name)
        selenium_action.action_fill_input(locator_field_user_password, data_password)
        selenium_action.action_click_element(locator_button_close_2)
    yield login_function

