from PageObjectModel import PageObjectModel
from robot.api.deco import not_keyword

class ProductsPageObject(PageObjectModel):

    def __init__(self):
        PageObjectModel.__init__()
        self.search = ''
        self.search_button = ''
        self.products_list = ''
        self.get_product_element = lambda product: [element for element in self.find_elements(self.products_list) if element.text() == product][0]
        self.continue_shopping_button = ''

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
        product_element.location_once_scrolled_into_view()
    
    @not_keyword
    def click_product_add_to_cart_on_products(self, produc:str) -> None:  
        self.log(f'Click {produc}\'s "Add to Cart"')
        product_element = self.get_product_element(produc)
        product_element.click()
    
    @not_keyword
    def click_continue_shopping_on_dialog_on_products(self) -> None: 
        self.log(f'"Continue Shopping" button locator: {self.continue_shopping_button}')
        self.click_button(self.continue_shopping_button)
