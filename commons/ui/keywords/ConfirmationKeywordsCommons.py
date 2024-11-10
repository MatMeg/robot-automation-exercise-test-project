from interfaces.PageInterfaces import ConfirmationPageObjectInterface
from robot.api.deco import keyword

class ConfirmationKeywordsCommons:
    def __init__(self, confirmation_page: ConfirmationPageObjectInterface):
        self._confirmation_page = confirmation_page

    @keyword('Order has been confirmed')
    def verify_order_confirmed(self):
        self._confirmation_page.verify_order_confirmed_on_confirmation()
        self._confirmation_page.take_screenshot('Verify order confirmed!')