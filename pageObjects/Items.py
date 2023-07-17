import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
class Items:
    button_add_to_cart_CSS = 'button.single_add_to_cart_button'
    textbox_item_quantity_CSS = 'input.input-text.qty.text'
    item_price_className = 'price'
    item_name_CSS = 'product_title.entry-title'
    item_category_className = 'posted_in'
    item_category_xpath = "//a[@rel='tag']"
    item_description_id = 'tab-description'
    page_item_container_xpath = '//*[@id="main"]/ul'
    items_nameTag = "li"
    button_add_from_home_xpath = '//*[@id="main"]/ul/li[{}]/a[2]'
    collection_pic_xpath = '//*[@id="product-34"]/div[1]/ol'


    def __init__(self, driver):
        self.driver = driver

    def clickAddToCart(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.button_add_to_cart_CSS).click()
            print("add to cart button found")
        except NoSuchElementException:
            print("add to cart button Not found!")
            assert False


    def setItemQuantity(self, amount):
        try:
         self.driver.find_element(By.CSS_SELECTOR, self.textbox_item_quantity_CSS).clear()
         self.driver.find_element(By.CSS_SELECTOR, self.textbox_item_quantity_CSS).send_keys(amount)
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

    def addItemFromHome(self,index):
        try:
            # xpath = self.button_add_from_home_xpath.format(index)
            self.driver.find_element(By.XPATH, f'//*[@id="main"]/ul/li[{index}]/a[2]' ).click()
            print("add to cart button found")
        except NoSuchElementException:
            print("add to cat button Not found!")
            assert False

    def viewCartAfterAdding(self):
        title_text = "View cart"
        try:
            self.driver.find_element(By.LINK_TEXT, title_text).click()
            print("view cart button found")

        except NoSuchElementException:
            print("view cart button Not found")
            assert False

    def viewCollectionPic(self):
        try:
            pic_element = self.driver.find_element(By.XPATH,self.collection_pic_xpath)
            li_elements = pic_element.find_elements(By.TAG_NAME, self.items_nameTag)
            for li_element in li_elements:
                li_element.click()
                time.sleep(2)
            print("collection picture found")
            print("num of items in collection: "+ str(len(li_elements)))
        except NoSuchElementException:
            assert False

    def getIntPrice(self,price):
        if " " in price:
            sale = price.split(" ")
            old_price = sale[0]
            new_price = sale[1]
            str = new_price.split("$")
        else:
            new_price = price
        str = new_price.split("$")
        float_price = float(str[1])
        print(float_price)

        return float_price