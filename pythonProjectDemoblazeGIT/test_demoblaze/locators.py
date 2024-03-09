from selenium.webdriver.common.by import By

"""КНОПКИ"""
locator_button_login_1 = (By.XPATH, '//*[@id="login2"]')
locator_button_login_2 = (By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
locator_button_sign_up_1 = (By.XPATH, '//*[@id="signin2"]')
locator_button_sign_up_2 = (By.XPATH, '/html/body/div[2]/div/div/div[3]/button[2]')
locator_button_home = (By.XPATH, '/html/body/nav/div[1]/ul/li[1]/a')

"""ФОРМЫ"""
locator_field_user_name = (By.XPATH, '//*[@id="loginusername"]')
locator_field_user_name_sign_up = (By.XPATH, '//*[@id="sign-username"]')
locator_field_user_password = (By.XPATH, '//*[@id="loginpassword"]')
locator_field_user_password_sign_up = (By.XPATH, '//*[@id="sign-password"]')

locator_user_logged_in_name = (By.XPATH, '//*[@id="nameofuser"]')




