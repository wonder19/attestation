#
# from pytest_testrail.plugin import pytestrail
#
# import allure
# from common.constants import PaymentPageConstants
# from model.payment import PaymentData
#
#
# class TestPayments:
#     @allure.suite("PaymentSuit")
#     @allure.tag("Testrail C12")
#     @pytestrail.case("C12")
#     def test_payment_between_wallets(self, login):
#         """
#             Steps.
#             1) Authorize
#             2) Click payment tab
#             3) Choose  payment between wallets link
#             4) Input date amount and comment values
#             5) Click continue button
#             6) Input summ
#             7) Click continue button
#             8) Accept conditions
#             9) Click continue button
#             """
#         payment_data = PaymentData().random()
#         login.open_main_page()
#         login.main_page.payment_button_click()
#         login.payment_page.between_wallets_link_click()
#         login.payment_page.fill_payment_inputs(payment_data)
#         assert (
#             login.payment_page.card_error_alert_get_text()
#             == "В демо-версии переводы не разрешены"
#         )
#
#     @allure.suite("PaymentSuit")
#     @allure.tag("Testrail C13")
#     @pytestrail.case("C13")
#     def test_input_smart_input(self, login):
#         """
#             Steps.
#             1) Authorize
#             2) Click payment tab
#             3) Click on dropdown
#             4) Input value into dropdown
#             """
#         input_dropdown_value = "ольга"
#         login.open_main_page()
#         login.main_page.payment_button_click()
#         login.payment_page.smart_payment_input_set_text(input_dropdown_value)
#         assert (
#             login.payment_page.smart_payment_dropdown_value_get_text()
#             == input_dropdown_value
#         )
#
#     @allure.suite("PaymentSuit")
#     @allure.tag("Testrail C14")
#     @pytestrail.case("C14")
#     def test_payment_between_wallets_with_empty_fields(self, login):
#         """
#             Steps.
#             1) Authorize
#             2) Click payment tab
#             3) Choose  payment between wallets link
#             4) Leave input fields empty
#             5) Click continue button
#             """
#         login.open_main_page()
#         login.main_page.payment_button_click()
#         login.payment_page.between_wallets_link_click()
#         login.payment_page.continue_button_click()
#         assert (
#             login.payment_page.empty_fields_alert_label_get_text()
#             == PaymentPageConstants.EMPTY_FIELD_ALERT
#         )
#
#     @allure.suite("PaymentSuit")
#     @allure.description("Payment without recipient card")
#     @allure.tag("Testrail C15")
#     @pytestrail.case("C15")
#     def test_card_payment_without_recipient_card(self, login):
#         """
#             Steps.
#             1) Authorize
#             2) Click payment tab
#             3) Choose  payment between wallets link
#             4) Leave inputs empty
#             5) Click continue button
#             """
#         login.open_main_page()
#         login.main_page.payment_button_click()
#         login.payment_page.on_card_payment_link_click()
#         login.payment_page.card_payment_amount_set_text("456456")
#         login.payment_page.continue_button_click()
#         assert (
#             login.payment_page.card_error_alert_get_text()
#             == PaymentPageConstants.SAME_CARD_ALERT
#         )
#
#     @allure.suite("PaymentSuit")
#     @allure.description("Payment between cards")
#     @allure.tag("Testrail C16")
#     @pytestrail.case("C16")
#     def test_card_payment(self, login):
#         """
#             Steps.
#             1) Authorize
#             2) Click payment tab
#             3) Choose  payment between wallets link
#             4) Fill card and amount values
#             5) Click continue button
#             """
#         login.open_main_page()
#         login.main_page.payment_button_click()
#         login.payment_page.on_card_payment_link_click()
#         login.payment_page.select_recipient_card("10061")
#         login.payment_page.card_payment_amount_set_text("456456")
#         login.payment_page.continue_button_click()
#         assert (
#             login.payment_page.card_payment_demo_alert_get_text()
#             == PaymentPageConstants.CARD_PAYMENT_DEMO_ALERT
#         )
#
#     @allure.suite("PaymentSuit")
#     @allure.description("Payment request")
#     @allure.tag("Testrail C17")
#     @pytestrail.case("C17")
#     def test_payment_request(self, login):
#         """
#             Steps.
#             1) Authorize
#             2) Click payment tab
#             3) Click request payment link
#             4) Input amount value
#             5) Click continue button
#             """
#         payment_data = PaymentData().random()
#         login.open_main_page()
#         login.main_page.payment_button_click()
#         login.payment_page.payment_request_link_click()
#         request_quantity = login.payment_page.get_request_quantity()
#         login.payment_page.fill_payment_request_values(payment_data)
#         login.payment_page.payment_request_popup_close_button_click()
#         new_request_quantity = login.payment_page.get_request_quantity()
#         assert (
#             login.payment_page.payment_success_alert_get_text()
#             == PaymentPageConstants.PAYMENT_REQUEST_SUCCESS_ALERT
#         )
#         assert new_request_quantity == request_quantity + 1
