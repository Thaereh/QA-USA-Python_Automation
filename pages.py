
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time
import data



class UrbanRoutesPage:
    FROM_FIELD= (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    CUSTOM_OPTION = ( By.XPATH, "//div[@class='mode active']")
    CALL_TAXI_BUTTON = (By.XPATH,"//button[contains(text(), 'Call a taxi')]")


    SUPPORTIVE_PLAN_LOCATOR=(By.XPATH, "//div[@class='tcard-title' and text()='Supportive']")
    SUPPORTIVE_PLAN_ACTIVE_LOCATOR=(By.XPATH,"//div[contains(@class,'tcard') and contains(@class, 'active') and .//div[@class='tcard-title' and text()='Supportive']]")
    supportive_plan_card = (By.XPATH, '//div[contains(text(), "Supportive")]')
    supportive_plan_card_parent = (By.XPATH, '//div[contains(text(), "Supportive")]//..')
    active_plan_card = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')

    OPEN_PHONE_FIELD = (By.XPATH,"//div[@class= 'np-text' and text()='Phone number']")
    PHONE_ACTIVE_SECTION=(By.XPATH,"//div[@class='section active' and text()='Enter your phone Number']")
    PHONE_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='+1 xxx xxx xx xx']")
    PHONE_INPUT_FALLBACK = (By.CSS_SELECTOR, "input[type='tel'], input[input mode='tel'], input[placeholder*='+1']")
    CLICK_NEXT_BUTTON = (By.XPATH, "//button[(@type='submit and text()='submit']")
    PHONE_SMS_FIELD=(By.XPATH,"//div[@class='head' and text()='Enter the code from the SMS']")
    PHONE_SMS_INPUT = (By.XPATH, "//input[@id='code' and //@placeholder='xxxx']")
    PHONE_SMS_INPUT_CONFIRM_BUTTON=(By.XPATH,"//input[@id='submit' and text()='Confirm']")
    INVALID_PHONE_SMS=(By.CLASS_NAME,'input-container-error')


    PAYMENT_METHOD_BUTTON = (By.XPATH, "//div[@class='Payment Method' and 'cash']")
    ADDING_CARD_FIELD =(By.XPATH,"//div[@class='pp-title' and text()='Add card')]")
    CLICK_ADD_CARD = (By.XPATH, "//div[@class='pp-plus-container']")
    CARD_ADD_DISPLAY=(By.XPATH,"//div[@class='head' and text()='Adding a card']")
    CARD_NUMBER_INPUT = (By.XPATH,"//div[@class='card-number-input' and //@placeholder='1234 0000 4321']")
    ENTER_CARD_CVV=(By.ID,"code")
    LINK_BUTTON=(By.XPATH,"//button[contains(text(),'Link') and @type='submit']")
    ADDED_CARD_VERIFICATION = (By.XPATH, "//div[@class='pp-img-container' and text()='Card']")

    COMMENT_INPUT_FIELD=(By.ID,'comment')
    MESSAGE_TO_DRIVER=(By.XPATH,"//input[@placeholder='Get some whiskey']")

    CLICK_ORDER_REQ=(By.XPATH,"//div[@class='reqs-head' and text()='Order Requirement']")
    ORDER_BLANKET_AND_HANDKERCHIEFS=(By.XPATH,"//div[text()='Blanket and handkerchiefs']")
    BLANKET_AND_HANDKERCHIEFS_SLIDER=(By.XPATH,"//span[@class='slider round']")
    BLANKET_AND_HANDKERCHIEFS_SWITCH=(By.XPATH,"//div[@class='switch']")

    ICE_CREAM_BUCKET=(By.XPATH,"//div[@class='r-group-tittle' and text()='Ice cream bucket']")
    ORDER_2_ICE_CREAMS=(By.XPATH, "//div[contains(@class, 'counter-plus')]")
    CHECK_2_ICE_CREAMS = (By.XPATH, "//div[contains(@class, 'counter-value')]")
    CLICK_ORDER = (By.XPATH, "//button[@type='button' and contains(., 'Enter the number and order')]")
    MODAL_LOCATOR=(By.XPATH,"//div[contains(@class,'order header content')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_from_address(self):
        self.driver.find_element(*self.FROM_FIELD).send_keys(data.ADDRESS_FROM)

    def set_to_address(self):
        self.driver.find_element(*self.TO_FIELD).send_keys(data.ADDRESS_TO)


    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.CALL_TAXI_BUTTON))

    def get_from_address(self):
            # Return the value from the "From" field
        return self.driver.find_element(*self.FROM_FIELD).get_property('value')

    def get_to_address(self):
            # Return the value from the "To" field
        return self.driver.find_element(*self.TO_FIELD).get_property('value')

    def select_supportive_plan(self):
        if self.driver.find_element(*self.supportive_plan_card_parent).get_attribute("class") != "tcard active":
            card = WebDriverWait(self.driver, 3).until(
                expected_conditions.visibility_of_element_located(self.supportive_plan_card))
            self.driver.execute_script("arguments[0].scrollIntoView();", card)
            card.click()

    def get_current_selected_plan(self):
        return self.driver.find_element(*self.SUPPORTIVE_PLAN_ACTIVE_LOCATOR).get_attribute('class')

    def get_supportive_plan_status(self):
        return self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR).get_attribute('class')

    def open_phone_field(self):
        self.wait.until(EC.element_to_be_clickable(self.OPEN_PHONE_FIELD)).click()

    def set_phone_number(self, number):
        self.driver.find_element(*self.OPEN_PHONE_FIELD).click()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(number)
        self.driver.find_element(*self.CLICK_NEXT_BUTTON).click()
        time.sleep(60)
        from helpers import retrieve_phone_code
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.PHONE_SMS_INPUT).send_keys(code)
        self.driver.find_element(*self.CLICK_NEXT_BUTTON).click()

    def get_phone_number(self):
        # Return the value from the "From" field
        return self.driver.find_element(*self.PHONE_NUMBER_INPUT).get_attribute('value')

    def enter_sms_code(self,code):
        sms_code_input = self.wait.until(EC.visibility_of_element_located(self.PHONE_SMS_FIELD))
        sms_code_input.clear()
        sms_code_input.send_keys(code)
        return sms_code_input

    def click_next_button(self)->None:
        self.wait.until(EC.element_to_be_clickable(self.CLICK_NEXT_BUTTON)).click()


    def click_confirm_button(self)->None:
        self.wait.until(EC.element_to_be_clickable(self.PHONE_SMS_INPUT_CONFIRM_BUTTON)).click()


    def add_card_and_get_method(self,number,code):
        self.driver.find_element(*self.PAYMENT_METHOD_BUTTON).click()
        self.driver.find_element(*self.ADDING_CARD_FIELD).click()
        self.driver.find_element(*self.CLICK_ADD_CARD).click()
        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(number)
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


    def get_ice_cream_count(self):
        el = self.wait.until(EC.visibility_of_element_located(self.CHECK_2_ICE_CREAMS))
        txt = el.text
        return txt

    def add_ice_creams(self):
        plus = self.wait.until(EC.element_to_be_clickable(self.ORDER_2_ICE_CREAMS))
        for i in range(2):
              plus.click()


    def order_taxi_supportive_tariff(self, number,message):
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()
        self.driver.find_element(*self.SUPPORTIVE_PLAN_ACTIVE_LOCATOR ).click()
        self.driver.find_element(*self.OPEN_PHONE_FIELD ).click()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(number)
        self.driver.find_element(*self.CLICK_NEXT_BUTTON).click()
        time.sleep(60)
        from helpers import retrieve_phone_code
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.PHONE_SMS_FIELD).send_keys(code)
        self.driver.find_element(*self.PHONE_SMS_INPUT_CONFIRM_BUTTON).click()
        self.driver.find_element(*self.MESSAGE_TO_DRIVER).send_keys(message)
        self.driver.find_element(*self.CLICK_ORDER).click()
        time.sleep(60)
        self.driver.find_element(*self.MODAL_LOCATOR)









