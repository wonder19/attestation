class MainPageConstants:
    USER_GREETING = "Hello World!"


class DepositPageConstants:
    PENS_ALERT_TEXT = 'Ольга, Вы еще не достигли пенсионного возраста. Если у вас есть пенсионное удостоверение,' \
                      ' обратитесь, пожалуйста, в любой офис Банка.'
    DEPOSIT_WITHOUT_END = 'свободный срок'

    currency_list = ['RUB', 'EUR', 'USD']
    end_date_list = ['15', '31', '91', '181', '367', '733', '-1']
    deposit_type = ['101']


class CardPageConstants:
    card_type = ['85', '150', '50', '55', '871', '872', '81', '82', '60', '83']
    SMS_INPUT_ERROR = 'Неверный код'
    SUCCESS_TITLE_TEXT = 'Ваша виртуальная карта готова! '
    SMS_CODE = '0000'
    SUCCESS_PHYSICAL_CARD_ALERT = 'Спасибо, ваша заявка принята. В ближайшее время ' \
                                  'вам поступит sms-сообщение о готовности карты с ' \
                                  'указанием места ее получения.'


class PaymentPageConstants:
    EMPTY_FIELD_ALERT = 'Не все поля заполнены корректно!'
    SAME_CARD_ALERT = 'Номера карт должны отличаться'
    CARD_PAYMENT_DEMO_ALERT = 'В демо-версии переводы не разрешены'
    PAYMENT_REQUEST_SUCCESS_ALERT = 'Ссылка сгенерирована'
