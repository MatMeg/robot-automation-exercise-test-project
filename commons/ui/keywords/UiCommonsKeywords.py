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
sys.path.append('./commons/ui/keywords/interfaces')
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
        CartKeywordsCommons.__init__(self,ui_commons)
        CheckoutKeywordsCommons.__init__(self,ui_commons)
        ConfirmationKeywordsCommons.__init__(self, ui_commons)
        DialogKeywordsCommons.__init__(self,ui_commons)
        LoginKeyWordsCommons.__init__(self,ui_commons)
        ModelKeywordsCommons.__init__(self,ui_commons)
        PaymentKeywordsCommons.__init__(self,ui_commons)
        ProductsKeywordsCommons.__init__(self,ui_commons)
        NavBarKeywordsCommons.__init__(self,ui_commons)
        _dialog_keyword_object = DialogKeywordsCommons(ui_commons)
        self.init_products_keywords_interfaces(_dialog_keyword_object) 
        self.init_login_keywords_interfaces(_dialog_keyword_object)   
    