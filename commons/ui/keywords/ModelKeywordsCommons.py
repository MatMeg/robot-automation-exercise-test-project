from robot.api.deco import keyword
from interfaces.PageInterfaces import BrowserInterface

class ModelKeywordsCommons:
    def __init__(self, page_object: BrowserInterface):
        self._page_object = page_object

    @keyword('Open "Automation Exercise" Page on Browser')
    def open_browser(self):
        url = self._page_object.get_url()
        browser = self._page_object.get_browse()
        self._page_object.log(f'<b>Open "{browser}" Browser</b>')
        self._page_object.log(f'<b>url:</b> {url}')
        self._page_object.open_browser_test_page(url)