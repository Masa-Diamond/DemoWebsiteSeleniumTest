from pageObjects.mainStorePage import MainStorePage
from pageObjects.LoginPage import Login
import time

class Test_login:
    baseURL = "http://demostore.supersqa.com/"
    email = "n@g.com"
    password = "123@456tredf#"
    wrong_password = "123@456yt@"
    at_index = email.find("@")
    username = email[:at_index]
    invalid_email = "n@@gmail.com"

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

    def testEmptyFields(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.lg_obj = Login(self.driver)
        self.main_obj.goToMyAccount()
        time.sleep(1)
        self.lg_obj.clickLogin()
        time.sleep(2)
        err = self.lg_obj.getError()
        print(err)
        if err == self.lg_obj.error_empty_field:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.close()

    def testNoPassword(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.lg_obj = Login(self.driver)
        self.main_obj.goToMyAccount()
        time.sleep(1)
        self.lg_obj.setUsername(self.email)
        time.sleep(2)
        self.lg_obj.clickLogin()
        time.sleep(2)
        err = self.lg_obj.getError()
        print(err)
        if err == self.lg_obj.error_no_password:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.close()

    def testWrongPassword(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.lg_obj = Login(self.driver)
        self.main_obj.goToMyAccount()
        time.sleep(1)
        self.lg_obj.setUsername(self.email)
        time.sleep(2)
        self.lg_obj.setPassword(self.wrong_password)
        time.sleep(2)
        self.lg_obj.clickLogin()
        time.sleep(2)
        err = self.lg_obj.getWrongPassError(self.email)
        print(err)
        #comparing the error msg is done within the get error funtion
        time.sleep(2)
        self.driver.close()

    def testInvalidUser(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.lg_obj = Login(self.driver)
        self.main_obj.goToMyAccount()
        time.sleep(1)
        self.lg_obj.setUsername(self.invalid_email)
        time.sleep(2)
        self.lg_obj.setPassword(self.password)
        time.sleep(2)
        self.lg_obj.clickLogin()
        time.sleep(2)
        err = self.lg_obj.getInvalidError(self.invalid_email)
        print(err)
        # comparing the error msg is done within the get error funtion
        time.sleep(2)
        self.driver.close()

    def testResetPassword(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.lg_obj = Login(self.driver)
        self.main_obj.goToMyAccount()
        self.lg_obj.clickLostPassword()
        time.sleep(2)
        self.lg_obj.setUsernameResetPass(self.email)
        time.sleep(1)
        self.lg_obj.clickResetPassword()
        time.sleep(2)
        msg = self.lg_obj.getMsgResetPassword()
        print(msg)
        if msg == self.lg_obj.msg_reset_password:
            assert True
        else:
            assert False
        time.sleep(2)
        self.driver.close()
