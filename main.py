import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class (cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        # Check the URL hasn't timed out

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route (self):
        #Vavigate
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.set_from_address()
        urban_routes_page.set_to_address()
        urban_routes_page.click_call_taxi_button()
        assert urban_routes_page.get_from_address()== data.ADDRESS_FROM
        assert urban_routes_page.get_to_address()==data.ADDRESS_TO

    def test_select_plan (self):
        #Navigate to app
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page=UrbanRoutesPage(self.driver)
        #actions
        urban_routes_page.set_from_address()
        urban_routes_page.set_to_address()
        time.sleep(2)
        urban_routes_page.click_call_taxi_button()
        time.sleep(2)
        #assertion
        supportive_status = urban_routes_page.select_supportive_plan()
        assert "active" in supportive_status

    def test_fill_phone_number (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_from_address()
        urban_routes_page.set_to_address()
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.set_phone_number(data.PHONE_NUMBER)
        time.sleep(2)
        from helpers import retrieve_phone_code
        code = retrieve_phone_code(self.driver)
        urban_routes_page.enter_sms_code(code)
        urban_routes_page.click_confirm_button()
        displayed_phone = urban_routes_page.get_phone_number()
        time.sleep(2)
        assert displayed_phone == data.PHONE_NUMBER

    def test_fill_card (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        wait = WebDriverWait(self.driver, 10)
        page.set_from_address()
        page.set_to_address()
        wait.until(EC.element_to_be_clickable(page.CALL_TAXI_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(page.SUPPORTIVE_PLAN_LOCATOR)).click()
        time.sleep(5)
        page.add_card_and_get_method(number='1234 5678 9100',code='1111')
        method_text = page.add_card_and_get_method('1234 5678 9100', '1111')
        assert "Card" in method_text

    def test_comment_for_driver(self):
        # Navigate
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        wait = WebDriverWait(self.driver, 10)
        page.set_from_address()
        page.set_to_address()
        wait.until(EC.element_to_be_clickable(page.CALL_TAXI_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(page.SUPPORTIVE_PLAN_LOCATOR)).click()
        page.comment_for_driver(data.MESSAGE_FOR_DRIVER).send_keys(data.MESSAGE_FOR_DRIVER)
        actual_message =page.comment_for_driver(data.MESSAGE_FOR_DRIVER).get_attribute('value')
        assert actual_message == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        wait = WebDriverWait(self.driver, 10)
        page.set_from_address()
        page.set_to_address()
        wait.until(EC.element_to_be_clickable(page.CALL_TAXI_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(page.SUPPORTIVE_PLAN_LOCATOR)).click()
        is_selected = page.order_blanket_and_handkerchiefs()
        assert is_selected == True

    def test_order_2_ice_creams (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        wait = WebDriverWait(self.driver, 10)

        page.set_from_address()
        page.set_to_address()
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
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(driver)
        wait=WebDriverWait(driver,15)
        #1Enter addresses
        page.set_from_address()
        page.set_to_address()
        #2click call taxi
        wait.until(EC.element_to_be_clickable(page.CALL_TAXI_BUTTON)).click()
        #3Select Supportive plan
        wait.until(EC.element_to_be_clickable(page.SUPPORTIVE_PLAN_LOCATOR)).click()
        #4 Enter Phone number
        wait.until(EC.element_to_be_clickable(page.OPEN_PHONE_FIELD)).click()
        wait.until(EC.visibility_of_element_located(page.PHONE_NUMBER_INPUT)).send_keys(data.PHONE_NUMBER)
        wait.until(EC.element_to_be_clickable(page.CLICK_NEXT_BUTTON)).click()
        #5 retrieve the SMS code via helper and confirm
        code = helpers.retrieve_phone_code(driver)
        wait.until(EC.visibility_of_element_located(page.PHONE_SMS_FIELD)).send_keys(code)
        wait.until(EC.element_to_be_clickable(page.PHONE_SMS_INPUT_CONFIRM_BUTTON)).click()
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
