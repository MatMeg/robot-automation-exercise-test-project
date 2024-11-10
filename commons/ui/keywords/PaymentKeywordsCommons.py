from interfaces.PageInterfaces import PaymentPageObjectInterface
from robot.api.deco import keyword

class PaymentKeywordsCommons:

    def __init__(self, payment_object: PaymentPageObjectInterface):
        self._payment_object = payment_object

    @keyword('Confirm payment with card "${card}"')
    def confirm_card_payment(self, card:dict):
        self._payment_object.log(f'<b>Card information:</b> {card}')
        self._payment_object.log('Input card name')
        self._payment_object.input_card_name_on_payment(card['name'])
        self._payment_object.log('Input card number')
        self._payment_object.input_card_name_on_payment(card['number'])
        self._payment_object.log('Input card cvv')
        self._payment_object.input_card_name_on_payment(card['cvv'])
        self._payment_object.log('Input card expiration month')
        self._payment_object.input_card_name_on_payment(card['MM'])
        self._payment_object.log('Input card expiration year')
        self._payment_object.input_card_name_on_payment(card['YYYY'])
        self._payment_object.take_screenshot('Click "Pay and Confirm"')
        self._payment_object.click_pay_and_confirm_on_payment()

    