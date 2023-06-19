from pageObjects.mainStorePage import MainStorePage
from pageObjects.LoginPage import Login
import time

class Test_login:
    baseURL = "http://demostore.supersqa.com/"
    email = "n@g.com"
    password = "123@456tredf#"
    at_index = email.find("@")
    username = email[:at_index]

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.lg_obj = Login(self.driver)
        self.main_obj.goToMyAccount()
        time.sleep(1)
        self.lg_obj.setUsername(self.email)
        time.sleep(2)
        self.lg_obj.setPassword(self.password)
        time.sleep(2)
        self.lg_obj.clickLogin()
        time.sleep(2)
        user = self.lg_obj.getUser()
        if user == self.username:
            print("Login success!")
            assert True
        else:
            assert False
        time.sleep(2)
        self.lg_obj.clickLogout()
        time.sleep(2)
        self.driver.close()