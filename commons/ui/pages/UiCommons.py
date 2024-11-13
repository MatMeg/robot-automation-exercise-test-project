from CartPageObject import CartPageObject
from CheckoutPageObject import CheckoutPageObject
from ConfirmationPageObject import ConfirmationPageObject
from LoginPageObject import LoginPageObject
from NavBarPageObject import NavBarPageObject
from PaymentPageObject import PaymentPageObject
from ProductsPageObject import ProductsPageObject
from robot.libraries.BuiltIn import BuiltIn
from Browser import Browser
import sys
sys.path.append('./resources/config')
from Configuration import AUTOMATION_EXERCISE_URL, BROWSER, DRIVER_PATH

class UiCommons(Browser, 
                CartPageObject, 
                CheckoutPageObject, 
                ConfirmationPageObject, 
                LoginPageObject,
                NavBarPageObject, 
                PaymentPageObject, 
                ProductsPageObject):
    
    def __init__(self):
        built_in = BuiltIn()
        Browser.__init__(self, built_in, AUTOMATION_EXERCISE_URL, BROWSER, DRIVER_PATH)
        CartPageObject.__init__(self, built_in)
        CheckoutPageObject.__init__(self, built_in)
        ConfirmationPageObject.__init__(self, built_in)
        LoginPageObject.__init__(self, built_in)
        NavBarPageObject.__init__(self, built_in)
        PaymentPageObject.__init__(self, built_in)
        ProductsPageObject.__init__(self, built_in)

        