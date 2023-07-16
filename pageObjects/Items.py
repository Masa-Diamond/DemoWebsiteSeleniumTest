from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Items:

    button_add_to_cart_className = 'single_add_to_cart_button button alt'
    textbox_item_quantity_className = 'input-text qty text'
    item_price_className = 'price'
    item_name_CSS = 'product_title.entry-title'
    item_category_className = 'posted_in'
    item_category_xpath = "//a[@rel='tag']"
    item_description_id = 'tab-description'
    page_item_container_xpath = '//*[@id="main"]/ul'
    items_nameTag = "li"


    def __init__(self, driver):
        self.driver = driver

    def clickAddToCart(self):
        try:
            self.driver.find_element(By.CLASS_NAME, self.button_add_to_cart_className).click()
            print("add to cart button found")
        except NoSuchElementException:
            print("add to cart button Not found!")
            assert False


    def setItemQuantity(self, amount):
        try:
         self.driver.find_element(By.CLASS_NAME, self.textbox_item_quantity_className).send_keys(amount)
         print("quantity textbox found")
        except NoSuchElementException:
            print("quantity textbox Not found!")
            assert False

    def getItemPrice(self):
        try:
            price =self.driver.find_element(By.CLASS_NAME, self.item_price_className).text
            print("price found")
            return price
        except NoSuchElementException:
            print("price Not found!")
            assert False

    def getItemName(self):
        try:
            name = self.driver.find_element(By.CLASS_NAME, self.item_name_CSS).text
            print("name found")
            return name
        except NoSuchElementException:
            print("name Not found!")
            assert False

    def getItemCategory(self):
        try:
            category = self.driver.find_element(By.CLASS_NAME, self.item_category_className).text
            print("category found")
            return category
        except NoSuchElementException:
            print("category Not found!")
            assert False

    def getItemDescription(self):
        try:
            description = self.driver.find_element(By.ID, self.item_description_id).text
            print("description found")
            return description
        except NoSuchElementException:
            print("description Not found!")
            assert False

    def goToCategory(self, category):
        try:
            partial_text = category
            self.driver.find_element(By.XPATH, f"//a[contains(text(), '{partial_text}')]").click()
            print("category link found")
        except NoSuchElementException:
            print("category link Not found!")
            assert False

    def getItemsCount(self):
        try:
            ul_element = self.driver.find_element(By.XPATH, self.page_item_container_xpath)
            li_elements = ul_element.find_elements(By.TAG_NAME, self.items_nameTag)
            num_li_elements = len(li_elements)
            return num_li_elements
        except NoSuchElementException:
            print("couldn't count items!")
            assert False