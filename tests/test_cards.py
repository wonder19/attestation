import time

import allure
import pytest
from pytest_testrail.plugin import pytestrail

from common.constants import CardPageConstants


class TestCards:
    @allure.suite("CardSuite")
    @allure.description("Order debet physical card test")
    @allure.tag("Testrail C7")
    @pytestrail.case("C7")
    @pytest.mark.skip
    @pytest.mark.parametrize('card_type, office_adress_value',
                             [('50', '001-055'), ('60', '001-056')])
    def test_order_debet_physical_card(self, login, card_type, office_adress_value):
        """
        Steps.
        1) Authorize
        2) Card tab
        3) Click order new debet card
        4) Choose office
        5) Confirm sms-code
        6) Click continue button
        """
        login.open_main_page()

        login.main_page.cards_button_click()
        login.card_page.order_new_card_button_click()
        login.card_page.new_debet_card_type_button_click(card_type)
        login.card_page.office_selection_dropdown_input(office_adress_value)
        login.card_page.order_button_click()
        login.card_page.sms_conformation(CardPageConstants.SMS_CODE)
        assert login.card_page.card_success_alert_get_text() == CardPageConstants.SUCCESS_PHYSICAL_CARD_ALERT

    @allure.suite("CardSuite")
    @allure.description("Order new virtual card test")
    @allure.tag("Testrail C8")
    @pytestrail.case("C8")
    def test_order_new_virtual_card(self, login):
        """
        Steps.
        1) Authorize
        2) Card tab
        3) Click order new card
        4) Click on virtual card
        5) Click on submit button
        6) Input summ
        7) Click continue button
        8) Accept conditions
        9) Click continue button
        """
        login.open_main_page()

        login.main_page.cards_button_click()
        login.card_page.order_new_card_button_click()
        login.card_page.new_virtual_card_type_button_click()
        login.card_page.submit_button_click()
        login.card_page.virtual_condition_checkbox_click()
        time.sleep(5)
        login.card_page.sms_conformation(CardPageConstants.SMS_CODE)
        assert login.card_page.success_title_get_text() == CardPageConstants.SUCCESS_TITLE_TEXT

    @allure.suite("CardSuite")
    @allure.description("Incorrect confirm sms code")
    @allure.tag("Testrail C9")
    @pytestrail.case("C9")
    @pytest.mark.parametrize('sms_code', ['1111', 'gjghgj', ''])
    def test_order_new_virtual_card_with_incorrect_sms_code(self, login, sms_code):
        """
        Steps.
        1) Authorize
        2) Card tab
        3) Click order new card
        4) Click on virtual card
        5) Click on submit button
        6) Input summ
        7) Click continue button
        8) Accept conditions
        9) Click continue button
        """
        login.open_main_page()

        login.main_page.cards_button_click()
        login.card_page.order_new_card_button_click()
        login.card_page.new_virtual_card_type_button_click()
        login.card_page.submit_button_click()
        login.card_page.virtual_condition_checkbox_click()
        login.card_page.sms_conformation(sms_code)
        assert CardPageConstants.SMS_INPUT_ERROR in login.card_page.error_label_get_text()

    @allure.suite("CardSuite")
    @allure.description("Sort cards by type")
    @allure.tag("Testrail C10")
    @pytestrail.case("C10")
    @pytest.mark.parametrize('card_type, type_name',
                             [('YARKO', 'Яркая'), ('RETIRED', 'Пенсионная'), ('VIRTUAL', 'Виртуальная')])
    def test_sort_cards_type(self, login, card_type, type_name):
        """
        Steps.
        1) Authorize
        2) Card tab
        3) Click order new card
        4) Click on sort dropdown
        5) Choose card type
        """
        login.open_main_page()
        login.main_page.cards_button_click()

        login.card_page.order_new_card_button_click()
        login.card_page.type_card_dropdown_select_value(card_type)
        assert login.card_page.type_card_title_label_get_text(card_type) == type_name

    @allure.suite("CardSuite")
    @allure.description("Order credit card")
    @allure.tag("Testrail C11")
    @pytestrail.case("C11")
    @pytest.mark.skip
    def test_order_new_credit_card(self, login):
        """
        Steps.
        1) Authorize
        2) Card tab
        3) Click order new credit card
        4) Input monthly income value
        5) Confirm acceptance in checkbox
        6) Click inspect button
        7) Confirm sms-code
        """
        login.open_main_page()

        login.main_page.cards_button_click()
        login.card_page.order_new_card_button_click()
        login.card_page.new_credit_card_type_button_click('85')

        login.card_page.fill_credit_card_information('50000')
        time.sleep(5)
        login.card_page.sms_conformation(CardPageConstants.SMS_CODE)
        # assert
