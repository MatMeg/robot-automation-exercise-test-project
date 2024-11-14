from PageObjectModel import PageObjectModel
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.remote.webelement import WebElement
from robot.api.deco import not_keyword

class ProductsPageObject(PageObjectModel):

    def __init__(self, builtIn : BuiltIn):
        PageObjectModel.__init__(self, builtIn)
        self.search_input = '//input[@id="search_product"]'
        self.search_button = '//button[@id="submit_search"]'
        self.products_list = '//div[@class="productinfo text-center"]/p'
        self.get_product_element = lambda product: '//*[text()=\"'+ product +'\"]/following-sibling::a'
        self.continue_shopping_button = '//button[text()="Continue Shopping"]'

    @not_keyword
    def input_search_criteria_on_products(self, search:str) -> None:  
        self.log(f'Search input locator: {self.search_input}')
        self.input_text(self.search_input, search)
    
    @not_keyword
    def click_search_icon_on_products(self) -> None: 
        self.log(f'"Search" button locator: {self.search_button}')
        self.click_button(self.search_button)
    
    @not_keyword
    def scroll_product_to_view_on_products(self, produc:str) -> None: 
        self.log(f'Scroll product "{produc}" into view')
        product_element = self.get_product_element(produc)
        self.wait_until_page_contains_element(product_element, '10s')
        self.scroll_element_into_view(product_element)
        self.take_screenshot('element_here')
    
    @not_keyword
    def click_product_add_to_cart_on_products(self, produc:str) -> None:  
        self.log(f'Click {produc}\'s "Add to Cart"')
        product_element = self.get_product_element(produc)
        self.click_button(product_element)
    
    @not_keyword
    def click_continue_shopping_on_dialog_on_products(self) -> None: 
        self.log(f'"Continue Shopping" button locator: {self.continue_shopping_button}')
        self.click_button(self.continue_shopping_button)
