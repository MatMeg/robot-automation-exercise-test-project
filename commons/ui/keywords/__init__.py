from robot.api.deco import keyword
from interfaces.PageInterfaces import UiCommonsInterface
from CartKeywordsCommons import CartKeywordsCommons
from CheckoutKeywordsCommons import CheckoutKeywordsCommons
from ConfirmationKeywordsCommons import ConfirmationKeywordsCommons
from DialogKeywordsCommons import DialogKeywordsCommons
from LoginKeywordsCommons import LoginKeyWordsCommons
from ModelKeywordsCommons import ModelKeywordsCommons
from PaymentKeywordsCommons import PaymentKeywordsCommons
from ProductsKeywordsCommons import ProductsKeywordsCommons
from NavBarKeywordsCommons import NavBarKeywordsCommons

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
        CartKeywordsCommons.__init__(ui_commons)
        CheckoutKeywordsCommons.__init__(ui_commons)
        ConfirmationKeywordsCommons.__init__(ui_commons)
        DialogKeywordsCommons.__init__(ui_commons)
        LoginKeyWordsCommons.__init__(ui_commons)
        ModelKeywordsCommons.__init__(ui_commons)
        PaymentKeywordsCommons.__init__(ui_commons)
        ProductsKeywordsCommons.__init__(ui_commons)
        NavBarKeywordsCommons.__init__(ui_commons)
        _dialog_keyword_object = DialogKeywordsCommons(ui_commons)
        self.init_products_keywords_interfaces(_dialog_keyword_object) 
        self.init_login_keywords_interfaces(_dialog_keyword_object)   
    