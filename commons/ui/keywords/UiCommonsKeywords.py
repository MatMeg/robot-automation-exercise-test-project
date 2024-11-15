import sys
from CartKeywordsCommons import CartKeywordsCommons
from CheckoutKeywordsCommons import CheckoutKeywordsCommons
from ConfirmationKeywordsCommons import ConfirmationKeywordsCommons
from DialogKeywordsCommons import DialogKeywordsCommons
from LoginKeywordsCommons import LoginKeyWordsCommons
from ModelKeywordsCommons import ModelKeywordsCommons
from PaymentKeywordsCommons import PaymentKeywordsCommons
from ProductsKeywordsCommons import ProductsKeywordsCommons
from NavBarKeywordsCommons import NavBarKeywordsCommons
from PageInterfaces import UiCommonsInterface

class UiCommonsKeywords(CartKeywordsCommons, 
                        CheckoutKeywordsCommons, 
                        ConfirmationKeywordsCommons, 
                        DialogKeywordsCommons, 
                        LoginKeyWordsCommons, 
                        ModelKeywordsCommons, 
                        PaymentKeywordsCommons, 
                        ProductsKeywordsCommons,
                        NavBarKeywordsCommons):
    def __init__(self, ui_commons: UiCommonsInterface):
        CartKeywordsCommons.__init__(self)
        CheckoutKeywordsCommons.__init__(self)
        ConfirmationKeywordsCommons.__init__(self)
        DialogKeywordsCommons.__init__(self)
        LoginKeyWordsCommons.__init__(self)
        ModelKeywordsCommons.__init__(self)
        PaymentKeywordsCommons.__init__(self)
        ProductsKeywordsCommons.__init__(self)
        NavBarKeywordsCommons.__init__(self)
        _nav_bar_obj = NavBarKeywordsCommons()
        _nav_bar_obj.init_nav_bar_keywords_interfaces(ui_commons)
        _dialog_obj = DialogKeywordsCommons()
        _dialog_obj.init_dialogs_keywords_interfaces(ui_commons)
        self.init_cart_keywords_interfaces(ui_commons)
        self.init_checkout_keywords_interfaces(ui_commons)
        self.init_confirmation_keywords_interfaces(ui_commons)
        self.init_dialogs_keywords_interfaces(ui_commons)
        self.init_login_keywords_interfaces(_nav_bar_obj, ui_commons)
        self.init_model_keywords_interfaces(ui_commons) 
        self.init_payment_keywords_interfaces(ui_commons)
        self.init_products_keywords_interfaces(_dialog_obj, ui_commons)
        self.init_nav_bar_keywords_interfaces(ui_commons) 

    def test_this_shit(self, producs):
        self.place_products_order(producs)
          
    