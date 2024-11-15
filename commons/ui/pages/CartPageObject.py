from PageObjectModel import PageObjectModel
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import not_keyword
from selenium.webdriver.remote.webelement import WebElement

class CartPageObject(PageObjectModel):

    def __init__(self, builtIn : BuiltIn):
        PageObjectModel.__init__(self, builtIn)
        self.products_elements = '//tr/td[@class="cart_description"]/h4/a'
        self.product_element=lambda i: f'//tr[{i}]/td[@class="cart_description"]/h4/a'
        self.proceed_to_checkout_button = 'document.querySelector("section#do_action").querySelector("a")'
        self.register_login_link = '//u[text()="Register / Login"]/parent::a[@href="/login"]'
    
    @not_keyword
    def verify_products_visible_on_cart(self, expected_products:list) -> None:
        expected_products_lower = [product.lower() for product in expected_products]
        self.log(f'Products elements locator: {self.products_elements}') 
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
    def click_proceed_to_checkout_on_cart(self) -> None:
        self.log(f'<b>"Proceed to Checkout"</b> button locator: {self.proceed_to_checkout_button}')
        self.click_with_java_script(self.proceed_to_checkout_button)

    @not_keyword
    def click_register_login_on_dialog_on_cart(self) -> None:
        self.log(f'"Register Login" link locator: {self.register_login_link}')
        self.wait_until_element_is_enabled(self.register_login_link)
        self.click_element(self.register_login_link)
