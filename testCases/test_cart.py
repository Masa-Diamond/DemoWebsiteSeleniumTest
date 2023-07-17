from pageObjects.mainStorePage import MainStorePage
from pageObjects.LoginPage import Login
from pageObjects.Items import Items
from pageObjects.CartPage import Cart
import time
import allure

class Test_cart:
    baseURL = "http://demostore.supersqa.com/"

    def test_back_to_shop(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.cart_obj = Cart(self.driver)
        self.main_obj.goToCart()
        time.sleep(2)
        self.cart_obj.clickReturnToShop()
        time.sleep(2)
        title = self.main_obj.getPageTtile()
        print(title)

    def test_adding_items_home(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.cart_obj = Cart(self.driver)
        self.item_obj = Items(self.driver)

        self.main_obj.goToHome()
        time.sleep(1)
        self.item_obj.addItemFromHome(2)
        self.item_obj.addItemFromHome(3)
        self.main_obj.goToNextPage()
        time.sleep(2)
        self.item_obj.addItemFromHome(4)
        time.sleep(2)
        self.item_obj.viewCartAfterAdding()
        print("view cart button works")
        count= self.cart_obj.getItemTableCount()
        if count == 3:
            print("num of items added: 3")
            assert True
        else:
            print("num of items: " + count)
            assert False

    def test_header_cart(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.cart_obj = Cart(self.driver)
        self.item_obj = Items(self.driver)
        time.sleep(2)
        info =self.cart_obj.getCurrentTotals()
        info = info.split(' ')
        price = info[0]
        items = info[1] + " " +info[2]
        print("the total price: " + price)
        print("the total item num added: " + items)


    def test_adding_items_search(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        total_price = float(0.00)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.cart_obj = Cart(self.driver)
        self.item_obj = Items(self.driver)
        self.main_obj.searchProduct("cap")
        price = self.item_obj.getItemPrice()
        total_price = total_price + self.item_obj.getIntPrice(price)
        time.sleep(1)
        self.item_obj.clickAddToCart()
        self.main_obj.searchProduct("album")
        price = self.item_obj.getItemPrice()
        total_price = total_price + self.item_obj.getIntPrice(price)
        time.sleep(1)
        self.item_obj.clickAddToCart()
        self.main_obj.searchProduct("Hoodie with Zipper")
        price = self.item_obj.getItemPrice()
        total_price = total_price + self.item_obj.getIntPrice(price)
        time.sleep(1)
        self.item_obj.clickAddToCart()
        time.sleep(2)
        info = self.cart_obj.getCurrentTotals()
        info = info.split(' ')
        price = info[0]
        price = self.item_obj.getIntPrice(price)
        items = int(info[1])

        if items == 3:
            print("num of items: 3")
        else:
            print("something is wrong with the items num!")
            assert False

        if price == total_price:
            print("total price: " + str(price))
        else:
            print("something wrong with the price calculations!")
            assert False


    def test_adding_multibles(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.cart_obj = Cart(self.driver)
        self.item_obj = Items(self.driver)
        self.item_obj.addItemFromHome(2)
        time.sleep(1)
        self.item_obj.addItemFromHome(2)
        time.sleep(1)
        self.item_obj.addItemFromHome(3)
        time.sleep(1)
        self.item_obj.addItemFromHome(3)
        time.sleep(1)
        self.main_obj.goToCart()
        products =self.cart_obj.getItemTableCount()
        print("num of products: " + str(products))
        info = self.cart_obj.getCurrentTotals()
        info = info.split(' ')
        items = info[1]
        print ("num of total items: " + items)
        #self.cart_obj.checkCartTotalPrice()

    def test_set_quantity(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.cart_obj = Cart(self.driver)
        self.item_obj = Items(self.driver)
        self.main_obj.searchProduct("cap")
        self.item_obj.setItemQuantity(3)
        time.sleep(1)
        self.item_obj.clickAddToCart()
        time.sleep(1)
        self.main_obj.searchProduct("sunglasses")
        self.item_obj.setItemQuantity(2)
        time.sleep(1)
        self.item_obj.clickAddToCart()
        self.main_obj.goToCart()
        self.cart_obj.checkQuantity()


    def test_cart_update(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.cart_obj = Cart(self.driver)
        self.item_obj = Items(self.driver)
        self.main_obj.searchProduct("cap")
        self.item_obj.setItemQuantity(3)
        time.sleep(1)
        self.item_obj.clickAddToCart()
        self.main_obj.goToCart()
        time.sleep(1)
        self.cart_obj.setNewQuantity(1,4)
        time.sleep(2)
        self.cart_obj.clickUpdateCart()

    def test_item_delete(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.cart_obj = Cart(self.driver)
        self.item_obj = Items(self.driver)
        self.main_obj.searchProduct("cap")
        self.item_obj.clickAddToCart()
        self.main_obj.searchProduct("belt")
        self.item_obj.clickAddToCart()
        self.main_obj.goToCart()
        time.sleep(1)
        self.cart_obj.deleteItem(1)
        time.sleep(2)
        self.cart_obj.clickUpdateCart()

    def test_coupon(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.cart_obj = Cart(self.driver)
        self.item_obj = Items(self.driver)
        self.main_obj.searchProduct("cap")
        self.item_obj.clickAddToCart()
        self.main_obj.goToCart()
        time.sleep(1)
        org_price = self.cart_obj.getFinalPrice()
        print("price before using coupon: " + org_price)
        time.sleep(1)
        self.cart_obj.setcoupon("SSQA100")
        time.sleep(1)
        self.cart_obj.clickApplyCoupon()
        time.sleep(2)
        alert = self.cart_obj.getCouponAlert()
        if alert == "Coupon code applied successfully.":
            print(alert)
        else:
            assert False
        new_price = self.cart_obj.getFinalPrice()
        print("price after using coupon: " + new_price)





