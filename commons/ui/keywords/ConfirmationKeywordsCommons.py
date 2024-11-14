import sys
from robot.api.deco import keyword, not_keyword
from PageInterfaces import ConfirmationPageObjectInterface


class ConfirmationKeywordsCommons:

    _confirmation_page:ConfirmationPageObjectInterface = None

    @keyword('Order has been confirmed')
    def verify_order_confirmed(self):
        self._confirmation_page.verify_order_confirmed_on_confirmation()
        self._confirmation_page.take_screenshot('Verify order confirmed!')

    @not_keyword
    def init_confirmation_keywords_interfaces(self, confirmation_page: ConfirmationPageObjectInterface) -> None:
        self._confirmation_page = confirmation_page