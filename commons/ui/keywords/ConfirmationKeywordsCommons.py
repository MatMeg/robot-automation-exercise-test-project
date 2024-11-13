import sys
from robot.api.deco import keyword
sys.path.append('./commons/ui/keywords/interfaces')
from PageInterfaces import ConfirmationPageObjectInterface


class ConfirmationKeywordsCommons:
    def __init__(self, confirmation_page: ConfirmationPageObjectInterface):
        self._confirmation_page = confirmation_page

    @keyword('Order has been confirmed')
    def verify_order_confirmed(self):
        self._confirmation_page.verify_order_confirmed_on_confirmation()
        self._confirmation_page.take_screenshot('Verify order confirmed!')