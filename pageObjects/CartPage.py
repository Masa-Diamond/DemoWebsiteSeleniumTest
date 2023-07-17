import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Cart:
  button_return_to_shop_className = "return-to-shop"
  view_cart_xpath = '//*[@id="site-header-cart"]/li[1]/a'
  info_current_cart_items_className = 'cart-contents'
  cart_items_table_xpath = '//*[@id="post-7"]/div/div/form/table/tbody'
  button_update_cart_CSS = 'button.button[name="update_cart"]'
  textbox_coupon_id = 'coupon_code'
  button_coupon_xpath = '//*[@id="post-7"]/div/div/form/table/tbody/tr[2]/td/div/button'
  alert_coupon_xpath = '//*[@id="post-7"]/div/div/div[1]/div'
  final_price_CSS = 'tr.order-total td[data-title="Total"]'



  def __init__(self, driver):
      self.driver = driver

  def clickReturnToShop(self):
      try:
          button = self.driver.find_element(By.CLASS_NAME, self.button_return_to_shop_className)
          print("return to shop button found")

          if button.is_enabled():
              print("Button is clickable")
              time.sleep(1)
              button.click()
          else:
              print("Button is not clickable")
      except NoSuchElementException:
          print("return to shop button Not fount!")
          assert False

  def viewCart(self):
      try:
          self.driver.find_element(By.XPATH, self.view_cart_xpath).click()
          print("view Cart button found")
      except NoSuchElementException:
          print("view Cart button Not fount!")
          assert False

  def getCurrentTotals(self):
      try:
         info = self.driver.find_element(By.CLASS_NAME, self.info_current_cart_items_className).text
         print("header cart info found")
         return info
      except NoSuchElementException:
          print("header cart info Not found!")
          assert False

  def getItemTableCount(self):
      try:
          table = self.driver.find_element(By.XPATH, self.cart_items_table_xpath)
          rows = table.find_elements(By.TAG_NAME,"tr")
          items = len(rows)-1
          print("items table found")
          return items

      except NoSuchElementException:
          print("coundn't find the table!")


  def checkQuantity(self):
      table = self.driver.find_element(By.XPATH, self.cart_items_table_xpath)
      rows = table.find_elements(By.TAG_NAME, "tr")
      for row in rows[:-1]:
          element = row.find_element(By.XPATH,'.//td[@class="product-quantity" and @data-title="Quantity"]//input[@type="number"]')
          value = element.get_attribute("value")
          print(value)

  def clickUpdateCart(self):
      try:
          self.driver.find_element(By.CSS_SELECTOR, self.button_update_cart_CSS).click()
          print("updatecart button found")
      except NoSuchElementException:
          print("update cart button Not found!")
          assert False

  def setNewQuantity(self,item,value):
      table = self.driver.find_element(By.XPATH, self.cart_items_table_xpath)
      rows = table.find_elements(By.TAG_NAME, "tr")

      row = rows[item-1]
      element = row.find_element(By.XPATH,'.//td[@class="product-quantity" and @data-title="Quantity"]//input[@type="number"]')
      element.clear()
      element.send_keys(str(value))
      print("quntity update")

  def deleteItem(self,item):
      table = self.driver.find_element(By.XPATH, self.cart_items_table_xpath)
      rows = table.find_elements(By.TAG_NAME, "tr")

      row = rows[item - 1]
      link = row.find_element(By.XPATH, './/a[@class="remove"]')
      link.click()
      print("item deleted")


  def setcoupon(self,value):
      try:
          self.driver.find_element(By.ID, self.textbox_coupon_id).send_keys(value)
          print("coupon textbox found")
      except NoSuchElementException:
          print("coupon textbox Not found!")

  def clickApplyCoupon(self):
      try:
          self.driver.find_element(By.XPATH,self.button_coupon_xpath).click()
          print("coupon button found")
      except NoSuchElementException:
          print ("coupon button Not found!")
          assert  False

  def getCouponAlert(self):
      try:
          text = self.driver.find_element(By.XPATH, self.alert_coupon_xpath).text
          print("alert found")
          return text

      except NoSuchElementException:
          print("alert Not found!")
          assert False

  def getFinalPrice(self):
      try:
          price = self.driver.find_element(By.CSS_SELECTOR, self.final_price_CSS).text
          print("final price found")
          return price
      except NoSuchElementException:
          print("final price not found")
          assert False



  # def checkCartTotalPrice(self):
  #     table = self.driver.find_element(By.XPATH, self.cart_items_table_xpath)
  #     #rows = table.find_elements(By.TAG_NAME, "tr")
  #     rows = self.driver.find_elements(By.XPATH, '//tr[position() < last()]')
  #     for row in rows:
  #         element = self.driver.find_element(By.CSS_SELECTOR, 'td.product-price[data-title="Price"]')
  #         price = element.text.strip().replace("$", "")
  #         print(price)
  #
  #         cells = row.find_elements(By.TAG_NAME,("td"))
  #         # value_price = float(cells[5].text.replace("$", "")) # Extract the value from column 4 and remove the "$" symbol
  #         # value_quantity = float(cells[6].text)
  #         # print(value_quantity)
  #         # total = float(cells[7].text.replace("$", "").replace(",", ""))
  #         # if total == value_price * value_quantity:
  #         #     print("Values match!")
  #         # else:
  #         #     print("Values do not match!")


