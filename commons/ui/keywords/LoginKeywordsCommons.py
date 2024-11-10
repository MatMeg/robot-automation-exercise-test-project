from interfaces.PageInterfaces import LoginPageObjectInterface, NavBarPageObjectInterface
from robot.api.deco import keyword

class LoginKeyWordsCommons:
    _navbar_page_object = None

    def __init__(self, login_page_object: LoginPageObjectInterface):
        self._login_page_object = login_page_object

    @keyword('Login with valid credendial "${account_dict}"')
    def login_to_account(self, account_dict:dict):
        '''
        '''
        user=account_dict['user']
        e_mail=account_dict['e-mail']
        password=account_dict['pass']
        self._login_page_object.log('<b>User Credentials:</b>')
        self._login_page_object.log(f'<b>User:</b> {user}')
        self._login_page_object.log(f'<b>E-mail:</b> {e_mail}')
        self._login_page_object.log(f'<b>Pass:</b> {password}')
        self._login_page_object.input_existing_account_user_on_login(e_mail)
        self._login_page_object.input_existing_account_pass_on_login(password)
        self._login_page_object.take_screenshot('Inputo credentials to existing account on <b>"Signup/Login"</b> page')
        self._login_page_object.log('Click <b>"Login"</b> button')
        self._login_page_object.click_login_on_login()
        self._navbar_page_object.verify_user_logged_in_on_navbar(user)
        self._login_page_object.take_screenshot(f'Verify user <b>{user.upper()}</b> was successfully logged')

    def init_login_keywords_interfaces(self, navbar_page_object : NavBarPageObjectInterface):
        self._navbar_page_object = navbar_page_object