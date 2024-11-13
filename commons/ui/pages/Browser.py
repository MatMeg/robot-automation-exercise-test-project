from PageObjectModel import PageObjectModel
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import not_keyword
import os

class Browser(PageObjectModel):

    def __init__(self, builtIn : BuiltIn, url: str, browser: str, driver_path: str):
        PageObjectModel.__init__(self, builtIn)
        self.url = url
        self.browser = browser
        self.driver_path = driver_path
    
    @not_keyword
    def open_browser_test_page(self):
        '''
        Open browser on "Automation Exercise" page
        '''
        os.environ["PATH"] += os.pathsep + self.driver_path
        print(f'{os.getenv("PATH")}')
        self.open_browser(url=self.url, browser=self.browser)
    
    @not_keyword
    def get_browse(self) -> str: 
        return str(self.browser)
    
    @not_keyword
    def get_url(self) -> str: 
        return str(self.url)