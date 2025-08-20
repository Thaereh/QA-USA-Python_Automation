import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import data
from data import PHONE_NUMBER
from data import CARD_CODE
from data import CARD_NUMBER
from data import MESSAGE_FOR_DRIVER
import helpers
import pages
from pages import UrbanRoutesPage
import pytest


class TestUrbanRoutes:
    @classmethod
    def __init__(self,driver):
        self.BLANKET_AND_HANDKERCHIEFS_SLIDER = (By.XPATH,"//span[@class='slider round']")
        self.MESSAGE_TO_DRIVER = (By.XPATH,"//input[@placeholder='Stop at the juice bar, please']")
        self.LINK_BUTTON = (By.XPATH,"//button[contains(text(),'Link') and @type='submit')]")
        self.ENTER_CARD_CVV = (By.ID,"code")
        self.ENTER_VALID_CARD_NUMBER = (By.ID,'number')
        self.ADDING_CARD_FIELD = (By.XPATH,"//div[contains(text(),'Add card')]")
        self.PAYMENT_METHOD = (By.XPATH, "//div[contains(text(),'Card')]")
        self.CHECK_2_ICE_CREAMS =(By.XPATH, "//div[contains(@class, 'counter-value')]")
        self.ORDER_2_ICE_CREAMS = (By.XPATH, "//div[contains(@class, 'counter-plus')]")
        self.CLICK_CONFIRM_BUTTON = (By.XPATH,"//button[contains(text(),'Confirm') and @type='submit']")
        self.CODE_INPUT_FIELD = (By.XPATH,"//input[@placeholder='xxxx']")
        self.CLICK_NEXT_BUTTON = (By.XPATH,"//button[contains(text(),'Next') and @type='submit']")
        self.PHONE_NUMBER_INPUT = (By.XPATH,"//input[@placeholder='+1 xxx xxx xx xx']")
        self.PHONE_FIELD = (By.CLASS_NAME,"np-text")
        self.driver = driver
        self.urban_routes_page = UrbanRoutesPage(driver)


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
        self.driver.get(data.URBAN_ROUTES_URL)
        print("function created for set route")
        pass
    def  test_select_plan (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page=UrbanRoutesPage(self.driver)
        page.set_from_address(data.ADDRESS_FROM)
        page.set_to_address(data.ADDRESS_TO)
        supportive_status=page.select_supportive_plan()
        assert "active" in supportive_status

    def test_fill_phone_number (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_from_address(data.ADDRESS_FROM)
        page.set_to_address(data.ADDRESS_TO)
        supportive_status = page.select_supportive_plan()
        self.driver.find_element(*self.PHONE_FIELD).click()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(PHONE_NUMBER)
        self.driver.find_element(*self.CLICK_NEXT_BUTTON).click()
        time.sleep(60)
        from helpers import retrieve_phone_code
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.CODE_INPUT_FIELD).send_keys(code)
        self.driver.find_element(*self.CLICK_CONFIRM_BUTTON).click()
        displayed_phone = self.driver.find_element(*self.PHONE_FIELD).text
        time.sleep(2)
        assert displayed_phone == PHONE_NUMBER

    def test_fill_card (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_from_address(data.ADDRESS_FROM)
        page.set_to_address(data.ADDRESS_TO)
        self.driver.find_element(*self.PAYMENT_METHOD).click()
        self.driver.find_element(*self.ADDING_CARD_FIELD).click()
        self.driver.find_element(*self.ENTER_VALID_CARD_NUMBER).send_keys(CARD_NUMBER)
        cvv_element = self.driver.find_element(*self.ENTER_CARD_CVV)
        cvv_element.send_keys(CARD_CODE)
        cvv_element.send_keys(Keys.TAB)
        self.driver.find_element(*self.LINK_BUTTON).click()
        actual_value = self.driver.find_element(*self.PAYMENT_METHOD).text
        assert actual_value == "Card"

    def test_comment_for_drive (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_from_address(data.ADDRESS_FROM)
        page.set_to_address(data.ADDRESS_TO)
        self.driver.find_element(*self.MESSAGE_TO_DRIVER).send_keys(MESSAGE_FOR_DRIVER)
        actual_message = self.driver.find_element(*self.MESSAGE_TO_DRIVER).get_attribute('value')
        assert actual_message == MESSAGE_FOR_DRIVER
    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_from_address(data.ADDRESS_FROM)
        page.set_to_address(data.ADDRESS_TO)
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_SLIDER).click()
        is_selected = self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_SLIDER).get_property('checked')
        assert is_selected == True
    def test_order_2_ice_creams (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_from_address(data.ADDRESS_FROM)
        page.set_to_address(data.ADDRESS_TO)
        supportive_status = page.select_supportive_plan()
        number_of_ice_creams = 2
        for i in range(2):
            self.driver.find_element(*self.ORDER_2_ICE_CREAMS).click()
        ice_cream_2_order = self.driver.find_element(*self.CHECK_2_ICE_CREAMS)
        assert ice_cream_2_order == "2"

        print("function created for order 2 ice creams")
            # Add in S8
        pass

    def test_car_search_model_appears (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_from_address(data.ADDRESS_FROM)
        page.set_to_address(data.ADDRESS_TO)
        supportive_status = page.select_supportive_plan()
        self.driver.find_element(*self.PAYMENT_METHOD).click()
        self.driver.find_element(*self.ADDING_CARD_FIELD).click()
        self.driver.find_element(*self.ENTER_VALID_CARD_NUMBER).send_keys(CARD_NUMBER)
        cvv_element = self.driver.find_element(*self.ENTER_CARD_CVV)
        cvv_element.send_keys(CARD_CODE)
        cvv_element.send_keys(Keys.TAB)
        self.driver.find_element(*self.LINK_BUTTON).click()
        actual_value = self.driver.find_element(*self.PAYMENT_METHOD).text
        assert actual_value == "Card"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
