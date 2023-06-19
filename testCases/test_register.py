
from pageObjects.RegisterPage import Register
from pageObjects.mainStorePage import MainStorePage
from pageObjects.LoginPage import Login
import time

class Test_register:
    baseURL = "http://demostore.supersqa.com/"
    email = "n9@g.com"
    email2 = "n@g.com"
    email3 = "n94@g.com"
    password = "123@456tredf#"
    weak_password = "11"
    invalid_email = "m@"
    at_index = email.find("@")
    username = email[:at_index]

    def test_newAccount(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        #objets
        self.main_obj = MainStorePage(self.driver)
        self.reg_obj = Register(self.driver)
        self.lg_obj = Login(self.driver)

        self.main_obj.goToMyAccount()
        time.sleep(1)
        self.reg_obj.setEmail(self.email)
        time.sleep(2)
        self.reg_obj.setPassword(self.password)
        time.sleep(2)
        self.reg_obj.clickRegister()
        time.sleep(2)
        user = self.lg_obj.getUser()
        if user == self.username:
            print("Register success!")
            assert True
        else:
            assert False
        time.sleep(2)
        self.lg_obj.clickLogout()
        time.sleep(2)
        self.driver.close()

    def test_alreadyReg(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.reg_obj = Register(self.driver)
        self.lg_obj = Login(self.driver)
        self.main_obj.goToMyAccount()
        time.sleep(1)
        self.reg_obj.setEmail(self.email2)
        time.sleep(2)
        self.reg_obj.setPassword(self.password)
        time.sleep(2)
        self.reg_obj.clickRegister()
        time.sleep(2)
        err= self.reg_obj.getErrorRedister()
        if err == self.reg_obj.error_registerd:
            print(err)
            assert True
        else:
            print(err)
            assert False
        time.sleep(2)
        self.driver.close()


    def test_noPassword(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.reg_obj = Register(self.driver)
        self.lg_obj = Login(self.driver)
        self.main_obj.goToMyAccount()
        time.sleep(1)
        self.reg_obj.setEmail(self.email3)
        time.sleep(2)
        self.reg_obj.clickRegister()
        time.sleep(2)
        err = self.reg_obj.getErrorNoPassword()
        if err == self.reg_obj.error_no_password:
            print(err)
            assert True
        else:
            print(err)
            assert False
        time.sleep(2)
        self.driver.close()

    def test_weakPassword(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.reg_obj = Register(self.driver)
        self.lg_obj = Login(self.driver)
        self.main_obj.goToMyAccount()
        time.sleep(1)
        self.reg_obj.setEmail(self.email)
        time.sleep(2)
        self.reg_obj.setPassword(self.weak_password)
        time.sleep(2)
        self.reg_obj.clickRegister()
        time.sleep(2)
        err = self.reg_obj.getErrorWeakPassword()
        if err == self.reg_obj.error_weak_password:
            print(err)
            assert True
        else:
            print(err)
            assert False
        time.sleep(2)
        self.driver.close()

    def test_invalidEmail(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.reg_obj = Register(self.driver)
        self.lg_obj = Login(self.driver)
        self.main_obj.goToMyAccount()
        time.sleep(1)
        self.reg_obj.setEmail(self.invalid_email)
        time.sleep(2)
        self.reg_obj.setPassword(self.password)
        time.sleep(2)
        self.reg_obj.clickRegister()
        time.sleep(2)
        err = self.reg_obj.findRegisterTitle()
        if err:
            print("didn't register with invalid email")
            assert True
        else:
            print("invalid email accepted!")
            assert False
        time.sleep(2)
        self.driver.close()