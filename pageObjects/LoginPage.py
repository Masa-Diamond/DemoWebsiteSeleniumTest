from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Login:
    text_welcome_user_xpath = '//*[@id="post-9"]/div/div/div/p[1]/strong[1]'
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_xpath = '//*[@id="customer_login"]/div[1]/form/p[3]/button'
    link_logout_linktest = "Log out"
    welcome_username_xpath = '//*[@id="post-9"]/div/div/div/p[1]/strong[1]'

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
