from PageObjectModel import PageObjectModel
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import not_keyword

class PaymentPageObject(PageObjectModel):

    def __init__(self, builtIn : BuiltIn):
        PageObjectModel.__init__(self, builtIn)
        self.name_input = '//input[@name="name_on_card"]'
        self.number_input = '//input[@name="card_number"]'
        self.cvv_input = '//input[@name="cvc"]'
        self.month_input = '//input[@name="expiry_month"]'
        self.year_input = '//input[@name="expiry_year"]'
        self.pay_and_confirm_button = '//button[@id="submit"]'

    @not_keyword
    def input_card_name_on_payment(self, name:str) -> None: 
        self.log(f'Name input locator: {self.name_input}')
        self.input_text(self.name_input, name)
    
    @not_keyword
    def input_card_number_on_payment(self, number:str) -> None:  
        self.log(f'Name input locator: {self.number_input}')
        self.input_text(self.number_input, number)
    
    @not_keyword
    def input_card_cvv_on_payment(self, cvv:str) -> None:  
        self.log(f'Cvv input locator: {self.cvv_input}')
        self.input_text(self.cvv_input, cvv)
    
    @not_keyword
    def input_card_expiration_month_on_payment(self, month:str) -> None:  
        self.log(f'Month input locator: {self.month_input}')
        self.input_text(self.month_input, month)
    
    @not_keyword
    def input_card_year_on_payment(self, year:str) -> None:  
        self.log(f'Year input locator: {self.year_input}')
        self.input_text(self.year_input, year)
    
    @not_keyword
    def click_pay_and_confirm_on_payment(self) -> None: 
        self.log(f'"Pay and Confirm" button locator: {self.pay_and_confirm_button}')
        self.click_button(self.pay_and_confirm_button)    