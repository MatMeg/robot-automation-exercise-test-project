from PageObjectModel import PageObjectModel
from robot.api.deco import not_keyword

class NavBarPageObject(PageObjectModel):

    def __init__(self):
        PageObjectModel.__init__()
        self.products_icon = ''
        self.cart_icon = ''
        self.user_icon = ''

    @not_keyword
    def click_products_on_navbar(self) -> None:  
        self.log(f'"Products" icon locator: {self.products_icon}')
        self.click_element(self.products_icon)
    
    @not_keyword
    def click_cart_on_navbar(self) -> None:  
        self.log(f'"Cart" icon locator: {self.cart_icon}')
        self.click_element(self.cart_icon)
    
    @not_keyword
    def verify_user_logged_in_on_navbar(self, user:str) -> None:
        self.log(f'"User" icon locator: {self.user_icon}')
        self.element_text_should_be(self.user_icon, user)
