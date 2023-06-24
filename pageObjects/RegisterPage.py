
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class Register:
     textbox_email_id = "reg_email"
     textbox_password_id = "reg_password"
     button_register_xpath = '//*[@id="customer_login"]/div[2]/form/p[3]/button'

     error_registerd = "Error: An account is already registered with your email address. Please log in."
     error_no_password = "Error: Please enter an account password."
     error_weak_password_xpath = '//*[@id="customer_login"]/div[2]/form/p[2]/span/div'
     error_weak_password = "Very weak - Please enter a stronger password."
     register_title_xpath = '//*[@id="customer_login"]/div[2]/h2'
     error_empty_field = "Error: Please provide a valid email address."
     error_msg_xpath = '//*[@id="content"]/div/div[1]/ul/li'
     #constructer
     def __init__(self,driver):
        self.driver = driver

     def setEmail(self,email):
         try:
             self.driver.find_element(By.ID, self.textbox_email_id).clear()
             self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)
             print("email textbox found")
         except NoSuchElementException:
             print("email textbox not found!")
             assert False

     def setPassword(self,password):
         try:
             self.driver.find_element(By.ID, self.textbox_password_id).clear()
             self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
             print("password textbox found")
         except NoSuchElementException:
             print("password textbox not found!")
             assert False

     def clickRegister(self):
         try:
          self.driver.find_element(By.XPATH,self.button_register_xpath).click()
          print("register button found")
         except NoSuchElementException:
             print("register button  not found!")
             assert False

     def getError(self):
         try:
             msg_error = self.driver.find_element(By.XPATH, self.error_msg_xpath).text
             return msg_error

         except NoSuchElementException:
             print("couldn't find error message!")
         assert False



     def getErrorWeakPassword(self):
         try:
             msg_error = self.driver.find_element(By.XPATH, self.error_weak_password_xpath).text
             return msg_error

         except NoSuchElementException:
             print("couldn't find error message!")
         assert False

     def findRegisterTitle(self):
         try:
          self.driver.find_element(By.XPATH, self.register_title_xpath)
          return True
         except NoSuchElementException:
             return False

