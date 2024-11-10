from PageObjectModel import PageObjectModel
from robot.api.deco import not_keyword

class Browser(PageObjectModel):

    def __init__(self):
        PageObjectModel.__init__()
        self.url = self.builtIn.get_variable_value('${AUTOMATION_EXERCISE_URL}')
        self.browser = self.builtIn.get_variable_value('${BROWSER}')
        self.diver_path = self.builtIn.get_variable_value('${DRIVER_PATH}')
    
    @not_keyword
    def open_browser_test_page(self):
        '''
        Open browser on "Automation Exercise" page
        '''
        self.open_browser(url=self.url, browser=self.browser, executable_path=self.driver_path)
    
    @not_keyword
    def get_browse(self) -> str: 
        return str(self.browser)
    
    @not_keyword
    def get_url(self) -> str: 
        return str(self.url)