from PageObjectModel import PageObjectModel
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import not_keyword

class CartPageObject(PageObjectModel):

    def __init__(self, builtIn : BuiltIn):
        PageObjectModel.__init__(self, builtIn)
        self.products_elements = '//td[@class="cart_description"]/h4/a'
        self.proceed_to_checkout_button = '//a[contains(text(),"Proceed To Checkout")]'
        self.register_login_link = '//u[text()="Register / Login"]/parent::a[@href="/login"]'
    
    @not_keyword
    def verify_products_visible_on_cart(self, expected_products:list) -> None:
        expected_products_lower = [product.lower() for product in expected_products]
        self.log(f'Products elements locator: {self.products_elements}') 
        listed_products = [element.text().lower() for element in self.find_elements(self.products_elements)]
        self.log(f'Listed products on page: {listed_products}')
        self.log(f'Expected products on page: {expected_products_lower}')
        self.builtIn.should_be_equal(len(listed_products), len(expected_products))
        for product in listed_products:
            self.builtIn.should_contain(expected_products_lower, product)

    @not_keyword
    def click_proceed_to_checkout_on_cart(self) -> None:
        self.log(f'"Proceed to Checkout" button locator: {self.proceed_to_checkout_button}')
        self.click_button(self.proceed_to_checkout_button)

    @not_keyword
    def click_register_login_on_dialog_on_cart(self) -> None:
        self.log(f'"Register Login" link locator: {self.proceed_to_checkout_button}')
        self.click_element(self.register_login_link)
