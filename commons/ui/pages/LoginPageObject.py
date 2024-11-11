from PageObjectModel import PageObjectModel
from robot.api.deco import not_keyword

class LoginPageObject(PageObjectModel):

    def __init__(self):
        PageObjectModel.__init__()
        self.e_mail_input = ''
        self.password_input = ''
        self.login_button = ''
    
    @not_keyword
    def input_existing_account_user_on_login(self, user: str) -> None:
        self.log(f'E-mail input locator: {self.e_mail_input}')
        self.input_text(self.e_mail_input, user)

    @not_keyword
    def input_existing_account_pass_on_login(self, password: str) -> None: 
        self.log(f'Password input locator: {self.password_input}')
        self.input_text(self.password_input, password)

    @not_keyword
    def click_login_on_login(self) -> None: 
        self.log(f'"Login" button locator: {self.login_button}')
        self.click_button(self.login_button)