import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from data import CARD_NUMBER, ADDRESS_FROM


class UrbanRoutesPage:
    FROM_FIELD= (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    CUSTOM_OPTION = ( By.XPATH, "//div[text()='Custom'}")
    CALL_TAXI_BUTTON = (By.XPATH,"//button[contains(text(), 'Call a taxi')]")
    SUPPORTIVE_PLAN_ACTIVE_LOCATOR = (By.XPATH, "//button[@data-for='tariff-card-4']/..")
    SUPPORTIVE_PLAN_LOCATOR = (By.XPATH, "//button[@data-for='tariff-card-4']")
    PHONE_FIELD= (By.CLASS_NAME,"np-text")
    PHONE_NUMBER_INPUT=(By.XPATH,"//input[@placeholder='+1 xxx xxx xx xx']")
    CLICK_NEXT_BUTTON=(By.XPATH,"//button[contains(text(),'Next') and @type='submit']")
    CODE_INPUT_FIELD =(By.XPATH,"//input[@placeholder='xxxx']")
    CLICK_CONFIRM_BUTTON= (By.XPATH,"//button[contains(text(),'Confirm') and @type='submit']")
    PAYMENT_METHOD = (By.XPATH, "//div[contains(text(),'Card')]")
    ADDING_CARD_FIELD =(By.XPATH,"//div[contains(text(),'Add card')]")
    CARD_INPUT = (By.CLASS_NAME,"card_input")
    ENTER_VALID_CARD_NUMBER=(By.ID,'number')
    ENTER_CARD_CVV=(By.ID,"code")
    LINK_BUTTON=(By.XPATH,"//button[contains(text(),'Link') and @type='submit')]")
    COMMENT_INPUT_FIELD=(By.ID,'comment')
    MESSAGE_TO_DRIVER=(By.XPATH,"//input[@placeholder='Stop at the juice bar, please']")
    ORDER_BLANKET_AND_HANDKERCHIEFS=(By.XPATH,"//div[text()='Blanket and handkerchiefs']")
    BLANKET_AND_HANDKERCHIEFS_SLIDER=(By.XPATH,"//span[@class='slider round']")
    ORDER_2_ICE_CREAMS=(By.XPATH, "//div[contains(@class, 'counter-plus')]")
    CHECK_2_ICE_CREAMS = (By.XPATH, "//div[contains(@class, 'counter-value')]")
    CLICK_ORDER=(By.XPATH,"//div[contains(@class,'order show')]")
    MODAL_LOCATOR=(By.XPATH,"//div[contains(@class,'order header content')]")

    def __init__(self, driver):
        self.driver = driver
    def set_from_address(self,address):
        self.driver.find_element(*self.FROM_FIELD).send_keys(address)
    def set_to_address(self,address):
        self.driver.find_element(*self.TO_FIELD).send_keys(address)
    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()

    def get_from_address(self):
            # Return the value from the "From" field
            return self.driver.find_element(*self.FROM_FIELD).get_attribute('value')

    def get_to_address(self):
            # Return the value from the "To" field
            return self.driver.find_element(*self.TO_FIELD).get_attribute('value')

    def select_supportive_plan(self):

        active_elements = self.driver.find_elements(*self.SUPPORTIVE_PLAN_ACTIVE_LOCATOR).get_attribute("class")

        if "active" in active_elements:
            print("Supportive Plan is already selected")
            pass
        else:
            supportive_button = self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR)
            supportive_button.click()

        selected_button = self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR)
        class_value = selected_button.get_property("className")
        return class_value



    def set_phone_number(self,number):
        self.driver.find_element(*self.PHONE_FIELD).click()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(number)
        self.driver.find_element(*self.CLICK_NEXT_BUTTON).click()
        time.sleep(60)
        from helpers import retrieve_phone_code
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.CODE_INPUT_FIELD).send_keys(code)
        self.driver.find_element(*self.CLICK_CONFIRM_BUTTON).click()
    def get_phone_number(self):
            # Return the value from the "From" field
            return self.driver.find_element(*self.PHONE_FIELD).get_attribute('value')

    def get_payment_method(self,number,code):
        self.driver.find_element(*self.PAYMENT_METHOD).click()
        self.driver.find_element(*self.ADDING_CARD_FIELD).click()
        self.driver.find_element(*self.ENTER_VALID_CARD_NUMBER).send_keys(number)
        cvv_element = self.driver.find_element(*self.ENTER_CARD_CVV)
        cvv_element.send_keys(code)
        cvv_element.send_keys(Keys.TAB)
        self.driver.find_element(*self.LINK_BUTTON).click()




    def comment_for_driver(self,message):
         self.driver.find_element(*self.MESSAGE_TO_DRIVER).send_keys(message)
         actual_message = self.driver.find_element(*self.MESSAGE_TO_DRIVER).get_attribute('value')


    def order_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_SLIDER).click()
        is_selected = self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_SLIDER).get_property('checked')


    def add_ice_creams(self):
        for i in range(2):
            self.driver.find_element(*self.ORDER_2_ICE_CREAMS).click()
        ice_cream_2_order=self.driver.find_element(*self.CHECK_2_ICE_CREAMS)

    def order_taxi_supportive_tariff(self, number,message):
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()
        self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR ).click()
        self.driver.find_element(*self.PHONE_FIELD).click()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(number)
        self.driver.find_element(*self.CLICK_NEXT_BUTTON).click()
        time.sleep(60)
        from helpers import retrieve_phone_code
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.CODE_INPUT_FIELD).send_keys(code)
        self.driver.find_element(*self.CLICK_CONFIRM_BUTTON).click()
        displayed_phone = self.driver.find_element(*self.PHONE_FIELD).text

        self.driver.find_element(*self.MESSAGE_TO_DRIVER).send_keys(message)
        self.driver.find_element(*self.CLICK_ORDER).click()
        time.sleep(60)
        modal_element=self.driver.find_element(*self.MODAL_LOCATOR)



