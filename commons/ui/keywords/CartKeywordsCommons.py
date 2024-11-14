from robot.api.deco import keyword, not_keyword
from PageInterfaces import CartPageObjectInterface


class CartKeywordsCommons:

    _cart_page_object : CartPageObjectInterface = None

    @keyword('Proceed to Checkout products "${products_list}"')
    def place_products_order(self, products_list:list):
        '''
        Verify expected products are visible on "Cart" page and then proceed to checkout
        :Args:
            products_list(list): list of expected products on checkout
        '''
        self._cart_page_object.take_screenshot(f'Verify the products: "{products_list}" are displayed on <b>Cart</b> page')
        self._cart_page_object.verify_products_visible_on_cart(products_list)
        self._cart_page_object.log('Click on <b>"Proceed to Checkout"</b> button')
        self._cart_page_object.click_proceed_to_checkout_on_cart()

    @not_keyword   
    def init_cart_keywords_interfaces(self, cart_page_objec: CartPageObjectInterface) -> None:
        self._cart_page_object = cart_page_objec

    