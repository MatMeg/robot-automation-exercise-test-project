from SeleniumLibrary import SeleniumLibrary
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import not_keyword
import time

class PageObjectModel(SeleniumLibrary):

    def __init__(self, builtIn : BuiltIn):
        SeleniumLibrary.__init__(self)
        self.builtIn = builtIn
    
    @not_keyword
    def log(self, msg:str):
        self.builtIn.log(f'<p>{msg}</p>',html=True)

    @not_keyword
    def take_screenshot(self, msg:str):
        self.log(msg)
        if self.builtIn.get_variable_value('${SCREENSHOT_ALLOWED}') :
            self.capture_page_screenshot(f'Selenium {time.time()}.png')