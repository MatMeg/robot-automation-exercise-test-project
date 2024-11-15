from robot.api.deco import keyword,not_keyword
from PageInterfaces import CheckoutPageObjectInterface

class CheckoutKeywordsCommons:
    
    _checkout_page_object : CheckoutPageObjectInterface = None        

    @keyword('Confirm "${products_list}" Order')
    def confirm_products_order(self, products_list:list):
        '''
        Verify expected products are visible on "Checkout" page and then place order
        :Args:
            products_list(list): list of expected products on checkout
        '''
        self._checkout_page_object.take_screenshot(f'Verify the products: "{products_list}" are displayed on <b>Checkout</b> page')
        self._checkout_page_object.verify_products_visible_on_checkout(products_list)
        self._checkout_page_object.log('Click on <b>"Place Order"</b> button')
        self._checkout_page_object.click_place_order_on_checkout()

    @not_keyword
    def init_checkout_keywords_interfaces(self, checkout_page_object: CheckoutPageObjectInterface) -> None:
        self._checkout_page_object = checkout_page_object
        

    