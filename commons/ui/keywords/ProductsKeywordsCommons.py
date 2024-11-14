from typing import Protocol
from robot.api.deco import keyword, not_keyword
from PageInterfaces import ProductsPageObjectInterface

class DialogKeywordsInterface(Protocol):
    def continue_shopping(self) -> None: ...


class ProductsKeywordsCommons:

    _dialog_keywords:DialogKeywordsInterface = None
    _products_object:ProductsPageObjectInterface = None

    @keyword('Add products "${products}" to cart (continue shopping)')
    def add_multiple_profiles_to_cart(self, products:list):
        self._products_object.log(f'Products to add: {products}')
        for product in products:
            self._products_object.scroll_product_to_view_on_products(product)
            self._products_object.take_screenshot(f'Add "{product}" to cart')
            self._products_object.click_product_add_to_cart_on_products(product)
            self._dialog_keywords.continue_shopping()

    @keyword('Search for "${serch_criteria}" on products')
    def search_for_product(self, search_criteria:str):
        self._products_object.input_search_criteria_on_products(search_criteria)
        self._products_object.click_search_icon_on_products()
        self._products_object.take_screenshot(f'Serch for <b>{search_criteria}</b>')

    @not_keyword
    def init_products_keywords_interfaces(self, 
                                          dialog_keywords:DialogKeywordsInterface, 
                                          products_object: ProductsPageObjectInterface) -> None:
        self._products_object = products_object
        self._dialog_keywords = dialog_keywords