import sys
from robot.api.deco import keyword
sys.path.append('./commons/ui/keywords/interfaces')
from PageInterfaces import NavBarPageObjectInterface

class NavBarKeywordsCommons:
    def __init__(self, navbar_page_object: NavBarPageObjectInterface):
        self._navbar_page_object = navbar_page_object

    @keyword('User "${user}" is logged in')
    def verify_user_successfully_loged(self, user:str):
        self._navbar_page_object.take_screenshot(f'Verify user <b>"{user}"</b> is logged in')
        self._navbar_page_object.verify_user_logged_in_on_navbar(user)

    @keyword('Select "${option}" on navbar')
    def select_option_on_navbar(self, option: str):
        option_lower_case = option.lower()
        self._navbar_page_object.take_screenshot(f'Select <b>{option_lower_case}</b> on navbar')
        if option_lower_case == 'products':
            self._navbar_page_object.click_products_on_navbar()
        elif option_lower_case == 'cart':
            self._navbar_page_object.click_cart_on_navbar()