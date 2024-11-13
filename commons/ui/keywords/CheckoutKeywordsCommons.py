import sys
from robot.api.deco import keyword
sys.path.append('./commons/ui/keywords/interfaces')
from PageInterfaces import CheckoutPageObjectInterface

class CheckoutKeywordsCommons:
    
    def __init__(self, checkout_page_object: CheckoutPageObjectInterface):
        self._checkout_page_object = checkout_page_object
        

    @keyword('Place Order of "${products_list}"')
    def place_products_order(self, products_list:list):
        '''
        Verify expected products are visible on "Checkout" page and then place order
        :Args:
            products_list(list): list of expected products on checkout
        '''
        self._checkout_page_object.take_screenshot(f'Verify the products: "{products_list}" are displayed on <b>Checkout</b> page')
        self._checkout_page_object.verify_products_visible_on_checkout(products_list)
        self._checkout_page_object.log('Click on <b>"Place Order"</b> button')
        self._checkout_page_object.click_place_order_on_checkout()
        

    