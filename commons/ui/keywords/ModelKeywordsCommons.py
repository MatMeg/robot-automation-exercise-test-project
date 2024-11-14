from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword, not_keyword
from PageInterfaces import BrowserInterface

class ModelKeywordsCommons:
    _page_object:BrowserInterface = None

    @keyword('Open "Automation Exercise" Page on Browser')
    def open_browser(self):
        url = self._page_object.get_url()
        browser = self._page_object.get_browse()
        self._page_object.log(f'<b>Open "{browser}" Browser</b>')
        self._page_object.log(f'<b>url:</b> {url}')
        self._page_object.open_browser_test_page()

    @not_keyword
    def init_model_keywords_interfaces(self, page_object: BrowserInterface) -> None:
        self._page_object = page_object