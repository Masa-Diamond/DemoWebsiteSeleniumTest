from selenium.webdriver.common.by import By

class MainStorePage:
    button_my_account_xpath = '//*[@id="site-navigation"]/div[1]/ul/li[4]/a'
    button_home_xpath = '//*[@id="site-navigation"]/div[1]/ul/li[1]/a'
    button_cart_xpath = '//*[@id="site-navigation"]/div[1]/ul/li[2]/a'
    button_checkout_xpath = '//*[@id="site-navigation"]/div[1]/ul/li[3]/a'
    button_sample_page_xpath = '//*[@id="site-navigation"]/div[1]/ul/li[5]/a'
    view_cart_xpath = '//*[@id="site-header-cart"]/li[1]/a'
    textbox_search_product_id = "woocommerce-product-search-field-0"

    def __init__(self, driver):
        self.driver = driver

    def goToMyAccount(self):
        self.driver.find_element(By.XPATH, self.button_my_account_xpath).click()

    def goToHome(self):
        self.driver.find_element(By.XPATH, self.button_home_xpath).click()

    def goToCart(self):
        self.driver.find_element(By.XPATH, self.button_cart_xpath).click()

    def goToCheckout(self):
        self.driver.find_element(By.XPATH, self.button_checkout_xpath).click()

    def goToSamplePage(self):
        self.driver.find_element(By.XPATH, self.button_sample_page_xpath).click()

    def viewCart(self):
        self.driver.find_element(By.XPATH, self.view_cart_xpath).click()

    def searchProduct(self, product):
        self.driver.find_element(By.ID, self.textbox_search_product_id).send_keys(product)