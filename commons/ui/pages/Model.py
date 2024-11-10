from PageObjectModel import PageObjectModel
from robot.api.deco import not_keyword

class CartPageObject(PageObjectModel):

    def __init__(self):
        PageObjectModel.__init__()
        self.products_elements = ''
        self.proceed_to_checkout_button = ''
    
    def verify_products_visible_on_cart(self, expected_products:list) :
        expected_products_lower = [product.lower() for product in expected_products] 
        listed_products = [element.text().lower() for element in self.find_elements(self.products_elements)]
        self.builtIn.should_be_equal(len(listed_products), len(expected_products))
        for product in listed_products:
            self.builtIn.should_contain(expected_products_lower, product)

    def click_proceed_to_checkout_on_cart(self):
        self.click_button(self.proceed_to_checkout_button)