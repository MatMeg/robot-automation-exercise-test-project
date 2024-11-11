from PageObjectModel import PageObjectModel
from robot.api.deco import not_keyword

class CheckoutPageObject(PageObjectModel):

    def __init__(self):
        PageObjectModel.__init__()
        self.products_elements = ''
        self.place_order_button = ''

    @not_keyword
    def verify_products_visible_on_checkout(self, expected_products:list) -> None:
        expected_products_lower = [product.lower() for product in expected_products]
        self.log(f'Products elements locator: {self.products_elements}') 
        listed_products = [element.text().lower() for element in self.find_elements(self.products_elements)]
        self.log(f'Listed products on page: {listed_products}')
        self.log(f'Expected products on page: {expected_products_lower}')
        self.builtIn.should_be_equal(len(listed_products), len(expected_products))
        for product in listed_products:
            self.builtIn.should_contain(expected_products_lower, product)

    @not_keyword
    def click_place_order_on_checkout(self) -> None:
        self.log(f'"Place Order" button locator: {self.place_order_button}')
        self.click_button(self.place_order_button)