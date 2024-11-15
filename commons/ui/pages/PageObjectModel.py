from SeleniumLibrary import SeleniumLibrary
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import not_keyword
import time

class PageObjectModel(SeleniumLibrary):

    def __init__(self, builtIn : BuiltIn):
        SeleniumLibrary.__init__(self)
        self.builtIn = builtIn
    
    @not_keyword
    def click_with_java_script(self, query_locator :str) -> None:
        script = 'try{\n'+ \
        f'{query_locator}.click();\n' +\
        'return true;\n'\
        '}catch(error){\n'\
        'return false;\n'\
        '}'
        self.execute_javascript(script)
    
    @not_keyword
    def log(self, msg:str):
        self.builtIn.log(f'<p>{msg}</p>',html=True)

    @not_keyword
    def take_screenshot(self, msg:str):
        self.log(msg)
        self.capture_page_screenshot(f'Selenium {time.time()}.png')