from PageObjectModel import PageObjectModel
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import not_keyword
from selenium.webdriver.remote.webelement import WebElement

class CheckoutPageObject(PageObjectModel):

    def __init__(self, builtIn : BuiltIn):
        PageObjectModel.__init__(self, builtIn)
        self.products_elements = '//td[@class="cart_description"]/h4/a'
        self.place_order_button = 'document.querySelector(\'a[href="/payment"]\')'

    @not_keyword
    def verify_products_visible_on_checkout(self, expected_products:list) -> None:
        expected_products_lower = [product.lower() for product in expected_products]
        self.log(f'Products elements locator: {self.products_elements}')
        self.scroll_element_into_view(self.products_elements) 
        number_elements = len(self.get_webelements(self.products_elements))
        listed_products = []
        for i in range(number_elements):
            listed_products.append(self.get_text(self.product_element(i+1)).lower())
        self.log(f'<b>Listed products on page</b>: {listed_products}')
        self.log(f'<b>Expected products on page</b>: {expected_products_lower}')
        self.builtIn.should_be_equal(len(listed_products), len(expected_products))
        for product in listed_products:
            self.builtIn.should_contain(expected_products_lower, product)

    @not_keyword
    def click_place_order_on_checkout(self) -> None:
        self.log(f'"Place Order" button locator: {self.place_order_button}')
        self.click_with_java_script(self.place_order_button)