from typing import Protocol

class PageObjectModelInterface(Protocol):
    def log(self, msg:str) -> None: ...
    def take_screenshot(self, msg:str) -> None: ...

class BrowserInterface(PageObjectModelInterface):
    def open_browser_test_page(self) -> None: ...
    def get_browse(self) -> str: ...
    def get_url(self) -> str: ...

class CartPageObjectInterface(PageObjectModelInterface):
    def verify_products_visible_on_cart(self, expected_products:list) -> None: ...
    def click_proceed_to_checkout_on_cart(self) -> None: ...

class CheckoutPageObjectInterface(PageObjectModelInterface):
    def verify_products_visible_on_checkout(self, expected_products:list) -> None: ...
    def click_place_order_on_checkout(self) -> None: ...

class DialogObjectInterface(PageObjectModelInterface):
    def click_continue_shopping_on_dialog_on_products(self) -> None: ...
    def click_register_login_on_dialog_on_cart(self) -> None: ...

class LoginPageObjectInterface(PageObjectModelInterface):
    def input_existing_account_user_on_login(self, user: str) -> None: ...
    def input_existing_account_pass_on_login(self, password: str) -> None: ...
    def click_login_on_login(self) -> None: ...

class PaymentPageObjectInterface(PageObjectModelInterface):
    def input_card_name_on_payment(self, name:str) -> None: ...
    def input_card_number_on_payment(self, number:str) -> None: ...
    def input_card_cvv_on_payment(self, cvv:str) -> None: ...
    def input_card_expiration_month_on_payment(self, month:str) -> None: ...
    def input_card_year_on_payment(self, year:str) -> None: ...
    def click_pay_and_confirm_on_payment(self) -> None: ...

class ProductsPageObjectInterface(PageObjectModelInterface):
    def input_search_criteria_on_products(self, search:str) -> None: ...
    def click_search_icon_on_products(self) -> None: ...
    def scroll_product_to_view_on_products(self, produc:str) -> None: ...
    def click_product_add_to_cart_on_products(self, produc:str) -> None: ...

class ConfirmationPageObjectInterface(PageObjectModelInterface):
    def verify_order_confirmed_on_confirmation(self) -> None: ...

class NavBarPageObjectInterface(PageObjectModelInterface):
    def click_products_on_navbar(self) -> None: ...
    def click_cart_on_navbar(self) -> None: ...
    def verify_user_logged_in_on_navbar(self, user:str) -> None: ...

class UiCommonsInterface(BrowserInterface, CartPageObjectInterface, CheckoutPageObjectInterface, DialogObjectInterface, PaymentPageObjectInterface, ProductsPageObjectInterface, ConfirmationPageObjectInterface):
    BrowserInterface.__init__()
    CartPageObjectInterface.__init__()
    CheckoutPageObjectInterface.__init__()
    DialogObjectInterface.__init__()
    PaymentPageObjectInterface.__init__()
    ProductsPageObjectInterface.__init__()
    ConfirmationPageObjectInterface.__init__()

    