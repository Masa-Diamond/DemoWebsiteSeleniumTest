from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Login:

    text_welcome_user_xpath = '//*[@id="post-9"]/div/div/div/p[1]/strong[1]'
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_xpath = '//*[@id="customer_login"]/div[1]/form/p[3]/button'
    link_logout_linktest = "Log out"
    welcome_username_xpath = '//*[@id="post-9"]/div/div/div/p[1]/strong[1]'
    error_msg_xpath = '//*[@id="content"]/div/div[1]/ul/li'
    error_empty_field = "Error: Username is required."
    error_no_password = "Error: The password field is empty."
    link_lost_password_linktest = "Lost your password?"
    msg_reset_password_xpath = '//*[@id="post-9"]/div/div/div'
    msg_reset_password = "Password reset email has been sent."
    textbox_reset_password_username_id = "user_login"
    button_reset_password_xpath = '//*[@id="post-9"]/div/div/form/p[3]/button'

    # constructer
    def __init__(self, driver):
        self.driver = driver

    def setUsername(self,username):
        try:
            self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)
            print("email textbox found")
        except NoSuchElementException:
            print("email textbox not found!")
            assert False

    def setPassword(self,password):
        try:
            self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
            print("password textbox found")
        except NoSuchElementException:
           print("password textbox not found!")
           assert False
    def clickLogin(self):
        try:
            self.driver.find_element(By.XPATH, self.button_login_xpath).click()
            print("login button found")
        except NoSuchElementException:
            print("login button  not found!")
            assert False
    def clickLogout(self):
        try:
            self.driver.find_element(By.LINK_TEXT, self.link_logout_linktest).click()
            print("log out button found")
        except NoSuchElementException:
            print("log out button  not found!")
            assert False
    def getUser(self):
        try:
             user = self.driver.find_element(By.XPATH, self.welcome_username_xpath).text
             return user
        except NoSuchElementException:
            print("login field!")
            assert False

    def getError(self):
        try:
            msg_error = self.driver.find_element(By.XPATH, self.error_msg_xpath).text
            return msg_error

        except NoSuchElementException:
            print("couldn't find error message!")
        assert False

    def getWrongPassError(self,username):
        error_wrong_password = f"Error: The password you entered for the email address {username} is incorrect. Lost your password?"
        try:
            msg_error = self.driver.find_element(By.XPATH, self.error_msg_xpath).text
            if msg_error == error_wrong_password:
                assert True
            else:
                assert False
            return msg_error

        except NoSuchElementException:
            print("couldn't find error message!")
        assert False

    def getInvalidError(self, username):
        error_wrong_password = f"Error: The username {username} is not registered on this site. If you are unsure of your username, try your email address instead."
        try:
            msg_error = self.driver.find_element(By.XPATH, self.error_msg_xpath).text
            if msg_error == error_wrong_password:
                assert True
            else:
                assert False
            return msg_error

        except NoSuchElementException:
            print("couldn't find error message!")
        assert False

    def clickLostPassword(self):
        try:
            self.driver.find_element(By.LINK_TEXT, self.link_lost_password_linktest).click()
            print("lost password button found")
        except NoSuchElementException:
            print("lost password button  not found!")
            assert False

    def clickResetPassword(self):
        try:
            self.driver.find_element(By.XPATH, self.button_reset_password_xpath).click()
            print("reset password button found")
        except NoSuchElementException:
            print("reset password button  not found!")
            assert False

    def setUsernameResetPass(self, username):
        try:
            self.driver.find_element(By.ID, self.textbox_reset_password_username_id).send_keys(username)
            print("email textbox found")
        except NoSuchElementException:
            print("email textbox not found!")
            assert False

    def getMsgResetPassword(self):
        try:
            msg = self.driver.find_element(By.XPATH, self.msg_reset_password_xpath).text
            return msg

        except NoSuchElementException:
            print("couldn't find error message!")
        assert False