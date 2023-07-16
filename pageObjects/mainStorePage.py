from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class MainStorePage:
    button_my_account_xpath = '//*[@id="site-navigation"]/div[1]/ul/li[4]/a'
    button_home_xpath = '//*[@id="site-navigation"]/div[1]/ul/li[1]/a'
    button_cart_xpath = '//*[@id="site-navigation"]/div[1]/ul/li[2]/a'
    button_checkout_xpath = '//*[@id="site-navigation"]/div[1]/ul/li[3]/a'
    button_sample_page_xpath = '//*[@id="site-navigation"]/div[1]/ul/li[5]/a'
    view_cart_xpath = '//*[@id="site-header-cart"]/li[1]/a'
    textbox_search_product_id = "woocommerce-product-search-field-0"
    check_item_home_page_xpath = '//*[@id="main"]/ul/li[4]'
    page_title_className = 'woocommerce-products-header'



    def __init__(self, driver):
        self.driver = driver

    def goToMyAccount(self):
        try:
         self.driver.find_element(By.XPATH, self.button_my_account_xpath).click()
         print("My account button found")
        except NoSuchElementException:
            print("My account button Not fount!")
            assert False

    def goToHome(self):
        try:
         self.driver.find_element(By.XPATH, self.button_home_xpath).click()
         print("Home button found")
        except NoSuchElementException:
         print("Home button Not fount!")
         assert False

    def goToCart(self):
        try:
         self.driver.find_element(By.XPATH, self.button_cart_xpath).click()
         print("cart button found")
        except NoSuchElementException:
         print("cart button Not fount!")
         assert False

    def goToCheckout(self):
        try:
          self.driver.find_element(By.XPATH, self.button_checkout_xpath).click()
          print("Check out button found")
        except NoSuchElementException:
         print("Check out button Not fount!")
         assert False

    def goToSamplePage(self):
        try:
         self.driver.find_element(By.XPATH, self.button_sample_page_xpath).click()
         print("Sample Page button found")
        except NoSuchElementException:
         print("Sample Page button Not fount!")
         assert False

    def viewCart(self):
        try:
         self.driver.find_element(By.XPATH, self.view_cart_xpath).click()
         print("view Cart button found")
        except NoSuchElementException:
         print("view Cart button Not fount!")
         assert False

    def searchProduct(self, product):
        try:
         self.driver.find_element(By.ID, self.textbox_search_product_id).send_keys(product )
         self.driver.find_element(By.ID, self.textbox_search_product_id).send_keys(Keys.RETURN)
         print("search bar found")
        except NoSuchElementException:
         print("search bar button Not fount!")
         assert False

    def checkItem(self):
        try:
            self.driver.find_element(By.XPATH, self.check_item_home_page_xpath).click()
            print("item found in home page")
        except NoSuchElementException:
            print("couldn't find item")
            assert False

    def getPageTtile(self):
        try:
            title =self.driver.find_element(By.CLASS_NAME, self.page_title_className).text
            print("title found")
            return title
        except NoSuchElementException:
            print("title Not found!")
            assert False