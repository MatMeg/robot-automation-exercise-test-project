from PageObjectModel import PageObjectModel
from robot.api.deco import not_keyword

class ConfirmationPageObject(PageObjectModel):

    def __init__(self):
        PageObjectModel.__init__()
        self.confirmation_text = ''

    @not_keyword
    def verify_order_confirmed_on_confirmation(self) -> None:
        expected_message = 'Congratulations! Your order has been confirmed!'
        self.log(f'Verify text \"{expected_message}\" is displayed on page')
        displayed_message = self.get_text(self.confirmation_text)
        self.builtIn.should_be_equal(expected_message, displayed_message)
        
