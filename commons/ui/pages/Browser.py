from PageObjectModel import PageObjectModel
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import not_keyword
import datetime


class Browser(PageObjectModel):

    def __init__(self, builtIn : BuiltIn, url: str, browser: str, options):
        PageObjectModel.__init__(self, builtIn)
        self.url = url
        self.browser = browser
        self.options = options
    
    @not_keyword
    def open_browser_test_page(self):
        '''
        Open browser on "Automation Exercise" page
        '''   
        self.open_browser(url=self.url, browser=self.browser, options=self.options)
        self.click_button('//button[@class="fc-button fc-cta-consent fc-primary-button"]')
    
    @not_keyword
    def get_browse(self) -> str: 
        return str(self.browser)
    
    @not_keyword
    def get_url(self) -> str: 
        return str(self.url)