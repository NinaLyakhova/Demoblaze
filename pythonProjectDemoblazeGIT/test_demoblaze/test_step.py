from Config.Config import *
from test_demoblaze.data import *
from test_demoblaze.locators import *


@pytest.fixture
def sign_up_form_demoblaze(browser, selenium_action):
    def sign_up_function():
        selenium_action.action_click_element(locator_button_sign_up_1)
        selenium_action.action_fill_input(locator_field_user_name_sign_up, data_user_name)
        selenium_action.action_fill_input(locator_field_user_password_sign_up, data_password)
        selenium_action.action_click_element(locator_button_sign_up_2)

    yield sign_up_function


@pytest.fixture
def login_form_demoblaze(browser, selenium_action):  # pytest -k login test_step.py

    def login_function():
        selenium_action.action_click_element(locator_button_login_1)
        selenium_action.action_fill_input(locator_field_user_name, data_user_name)
        selenium_action.action_fill_input(locator_field_user_password, data_password)
       # selenium_action.action_click_element(locator_button_login_2)

    yield login_function
