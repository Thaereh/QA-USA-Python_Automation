import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import helpers
from helpers import retrieve_phone_code
from pages import UrbanRoutesPage
import data

class TestUrbanRoutes:
    @classmethod
    def setup_class (cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route (self):
        #Vavigate
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        #actions
        urban_routes_page.set_from_address(data.ADDRESS_FROM)
        urban_routes_page.set_to_address(data.ADDRESS_TO)
        # assertion
        from_value = urban_routes_page.get_from_address()
        to_value = urban_routes_page.get_to_address()
        assert from_value == data.ADDRESS_FROM, f"Expected FROM address '{data.ADDRESS_FROM}', but got '{from_value}'"
        assert to_value == data.ADDRESS_TO, f"Expected TO address '{data.ADDRESS_TO}', but got '{to_value}'"

    def  test_select_plan (self):
        #Navigate to app
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page=UrbanRoutesPage(self.driver)
        #actions
        status = urban_routes_page.select_supportive_plan()
        urban_routes_page.set_to_address(data.ADDRESS_TO)

        #assertion
        supportive_status=urban_routes_page.get_supportive_plan_status()
        assert "active" in supportive_status,f"Expected 'active' in status, got '{status}'"


    def test_fill_phone_number (self):
        #Navigate
       self.driver.get(data.URBAN_ROUTES_URL)
       urban_routes_page = UrbanRoutesPage(self.driver)
        # actions
       urban_routes_page.set_from_address(data.ADDRESS_FROM)
       urban_routes_page.set_to_address(data.ADDRESS_TO)
       urban_routes_page.click_call_taxi_button()
       urban_routes_page.select_supportive_plan()
       urban_routes_page.set_phone_number(data.PHONE_NUMBER)
        #retrieve and enter SMS code
       code = retrieve_phone_code(data.PHONE_NUMBER)
       urban_routes_page.enter_sms_code(code)
       urban_routes_page.CLICK_CONFIRM_BUTTON()


       displayed_phone = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                urban_routes_page.PHONE_FIELD,  # locator tuple
                data.PHONE_NUMBER
            )
        )
       assert displayed_phone == data.PHONE_NUMBER, \
            f"Expected phone number '{data.PHONE_NUMBER}', but got '{displayed_phone}'"

    def test_fill_card (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        method_text = page.add_card_and_get_method('1234 5678 9100', '1111')
        assert method_text == "Card"

    def test_comment_for_driver(self):
        # Navigate
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_from_address(data.ADDRESS_FROM)
        page.set_to_address(data.ADDRESS_TO)
        #actions
        message = "Stop at the juice bar, please"
        actual_message = page.comment_for_driver(message)
        #assert
        assert actual_message == message


    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_from_address(data.ADDRESS_FROM)
        page.set_to_address(data.ADDRESS_TO)
        is_selected = page.order_blanket_and_handkerchiefs()
        assert is_selected == True

    def test_order_2_ice_creams (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        wait = WebDriverWait(self.driver, 10)

        page.set_from_address(data.ADDRESS_FROM)
        page.set_to_address(data.ADDRESS_TO)
        wait.until(EC.element_to_be_clickable(page.CALL_TAXI_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(page.SUPPORTIVE_PLAN_LOCATOR)).click()

        plus = wait.until(EC.element_to_be_clickable(page.ORDER_2_ICE_CREAMS))
        for i in range(2):
            plus.click()
        wait.until(EC.text_to_be_present_in_element(page.CHECK_2_ICE_CREAMS, "2"))
        count_el = wait.until(EC.visibility_of_element_located(page.CHECK_2_ICE_CREAMS))
        assert count_el.text.strip() == "2", f"Expected 2 ice creams, got '{count_el.text.strip()}'"
            # Add in S8


    def test_car_search_model_appears (self,driver):
        driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(driver)
        wait=WebDriverWait(driver,15)
        #1Enter addresses
        page.set_from_address(data.ADDRESS_FROM)
        page.set_to_address(data.ADDRESS_TO)
        #2click call taxi
        wait.until(EC.element_to_be_clickable(page.CALL_TAXI_BUTTON)).click()
        #3Select Supportive plan
        wait.until(EC.element_to_be_clickable(page.SUPPORTIVE_PLAN_LOCATOR)).click()
        #4 Enter Phone number
        wait.until(EC.element_to_be_clickable(page.PHONE_FIELD)).click()
        wait.until(EC.visibility_of_element_located(page.PHONE_NUMBER_INPUT)).send_keys(data.PHONE_NUMBER)
        wait.until(EC.element_to_be_clickable(page.CLICK_NEXT_BUTTON)).click()
        #5 retrieve the SMS code via helper and confirm
        code = helpers.retrieve_phone_code(driver)
        wait.until(EC.visibility_of_element_located(page.PHONE_SMS_FIELD)).send_keys(code)
        wait.until(EC.element_to_be_clickable(page.CLICK_CONFIRM_BUTTON)).click()
        #6 add a message for the driver
        message = "Stop at the juice bar, please"
        actual_message = page.comment_for_driver(message)
        assert actual_message == message, f"Expected message'{message}', but got {actual_message}'"
        #7 Click Order
        wait.until(EC.element_to_be_clickable(page.CLICK_ORDER)).click()
        # 8 Assert
        modal = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(page.MODAL_LOCATOR)
        )
        assert modal.is_displayed(),"Car search modal did not appear!"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
