import pytest

from test_demoblaze.test_step import *


class TestLogin:
    @pytest.mark.smoke  # pytest -k test_login_successful test_demoblaze.test_check
    def test_login_successful_demoblaze(self, browser, selenium_action, login_form_demoblaze):
        """Проверка входа"""
        login_form_demoblaze()
        selenium_action.action_wait_on_page(1000)
        assert "https://www.demoblaze.com/index.html" in browser.current_url.lower()
        print('Вход успешный')
        selenium_action.action_close_current_window()


