from pageObjects.RegisterPage import Register
from pageObjects.mainStorePage import MainStorePage
from pageObjects.LoginPage import Login
from pageObjects.Items import Items
import time

class Test_shopping:
    baseURL = "http://demostore.supersqa.com/"
    email = "n@g.com"
    password = "123@456tredf#"

    def get_product_info(self):
        name = self.item_obj.getItemName()
        print("product name: " + name)
        price = self.item_obj.getItemPrice()
        if " " in price:
            sale = price.split(" ")
            old_price = sale[0]
            new_price = sale[1]
            print("product old price: " + old_price)
            print("product new price: " + new_price)
        else:
            print("product proce: " + price)
        description = self.item_obj.getItemDescription()
        print("product description: " + description)
        category = self.item_obj.getItemCategory()
        print("product category: " + category)



    def test_searching(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.lg_obj = Login(self.driver)
        self.item_obj = Items(self.driver)

        self.main_obj.goToMyAccount()
        time.sleep(1)
        self.lg_obj.setUsername(self.email)
        time.sleep(2)
        self.lg_obj.setPassword(self.password)
        time.sleep(2)
        self.lg_obj.clickLogin()
        time.sleep(2)
        self.main_obj.searchProduct("cap")
        time.sleep(1)
        name =self.item_obj.getItemName().lower()
        if name == "cap":
            print("right item")
        else:
            print("didn't find the product")
            assert False
        self.main_obj.searchProduct("belt")
        time.sleep(1)
        name = self.item_obj.getItemName()
        if name.lower() == "belt":
            print("right item")
        else:
            print("didn't find the product")
            assert False
        self.main_obj.searchProduct("sunglasses")
        time.sleep(1)
        name = self.item_obj.getItemName()
        if name.lower() == "sunglasses":
            print("right item")
        else:
            print("didn't find the product")
            assert False

    def test_items_count(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.item_obj = Items(self.driver)
        self.main_obj.goToHome()
        time.sleep(1)
        count = self.item_obj.getItemsCount()
        print("items count page1: " + str(count))
        time.sleep(1)
        self.main_obj.goToNextPage()
        count = self.item_obj.getItemsCount()
        print("items count page2: " + str(count))



    def test_item_info(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.item_obj = Items(self.driver)
        self.main_obj.searchProduct("cap")
        time.sleep(1)
        self.get_product_info()
        print("items info are available from search")
        self.main_obj.goToHome()
        self.main_obj.checkItem()
        time.sleep(2)
        self.get_product_info()
        print("can go to item from home")


    def test_category_link(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.item_obj = Items(self.driver)
        self.main_obj.searchProduct("cap")
        time.sleep(1)
        partial_text = self.item_obj.getItemCategory()
        text = partial_text.split(" ")
        category = text[1]
        self.item_obj.goToCategory(category)
        title =self.main_obj.getPageTtile()

        if category == title:
            print("in " + category + " category page")
        else:
            assert False

        time.sleep(1)
        count = self.item_obj.getItemsCount()
        print("items count: " + str(count))

    def test_view_collection(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        # objets
        self.main_obj = MainStorePage(self.driver)
        self.item_obj = Items(self.driver)
        self.main_obj.searchProduct("Logo Collection")
        time.sleep(1)
        self.item_obj.viewCollectionPic()

