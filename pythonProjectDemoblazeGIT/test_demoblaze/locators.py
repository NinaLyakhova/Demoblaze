from selenium.webdriver.common.by import By

locator_button_login_1 = (By.XPATH, '//*[@id="login2"]')
locator_button_login_2 = (By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
locator_button_sign_up_1 = (By.XPATH, '//*[@id="signin2"]')
locator_button_sign_up_2 = (By.XPATH, '/html/body/div[2]/div/div/div[3]/button[2]')
locator_button_home = (By.XPATH, '/html/body/nav/div[1]/ul/li[1]/a')

locator_field_user_name = (By.XPATH, '//*[@id="loginusername"]')
locator_field_user_name_sign_up = (By.XPATH, '//*[@id="sign-username"]')
locator_field_user_password = (By.XPATH, '//*[@id="loginpassword"]')
locator_field_user_password_sign_up = (By.XPATH, '//*[@id="sign-password"]')

locator_user_logged_in_name = (By.XPATH, '//*[@id="nameofuser"]')

locator_categories_phones = (By.CSS_SELECTOR, 'a.list-group-item:nth-child(2)')
locator_categories_laptops = (By.CSS_SELECTOR, 'a.list-group-item:nth-child(3)')
locator_categories_monitors = (By.CSS_SELECTOR, 'a.list-group-item:nth-child(4)')

locator_select_phone_samsung = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[4]/div/div/h4/a')
locator_select_phone_iphone = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[5]/div/div/h4/a')

locator_select_laptop_MacBook_air = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[3]/div/div/h4/a')
locator_select_laptop_MacBook_pro = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[6]/div/div/h4/a')

locator_select_monitor_apple = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')
locator_select_monitor_asus = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a')


