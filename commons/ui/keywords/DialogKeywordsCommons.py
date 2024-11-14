import sys
from robot.api.deco import keyword
from PageInterfaces import DialogObjectInterface

class DialogKeywordsCommons:

    _dialog_object:DialogObjectInterface = None
    
    @keyword('Proceed to "Register/Login" from "Checkout" dialog on "Cart" Page')
    def proceed_to_login_from_cart(self):
        self._dialog_object.take_screenshot('Click on <b>"Register/Login"</b> link')
        self._dialog_object.click_register_login_on_dialog_on_cart()

    @keyword('Continue Shopping')
    def continue_shopping(self):
        self._dialog_object.take_screenshot('Click on <b>"Continue Shopping"</b> button')
        self._dialog_object.click_continue_shopping_on_dialog_on_products()

    def init_dialogs_keywords_interfaces(self, dialog_object : DialogObjectInterface):
        self._dialog_object = dialog_object