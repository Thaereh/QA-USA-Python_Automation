
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import data



class UrbanRoutesPage:
    FROM_FIELD= (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    CUSTOM_OPTION = ( By.XPATH, "//div[text()='Custom']")
    CALL_TAXI_BUTTON = (By.XPATH,"//button[contains(text(), 'Call a taxi')]")
    SUPPORTIVE_PLAN_CARD_PARENT=(By.XPATH, "//div[contains(@class,'tcard') and .//div[text()='Supportive']]")
    SUPPORTIVE_PLAN_LOCATOR=(By.XPATH, "//div[@class='tcard-title' and text()='Supportive']")
    SUPPORTIVE_PLAN_ACTIVE_LOCATOR = (By.XPATH, "//button[@data-for='tariff-card-4']/..")
    PHONE_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='+1 xxx xxx xx xx']")  # your original
    PHONE_INPUT_FALLBACK = (By.CSS_SELECTOR, "input[type='tel'], input[input mode='tel'], input[placeholder*='+1']")
    OPEN_PHONE_FIELD = (By.CLASS_NAME, "np-text")
    PHONE_FIELD = (By.CLASS_NAME, "np-text")
    PHONE_SMS_FIELD=(By.XPATH,"//input[@placeholder='xxxx']")
    CLICK_NEXT_BUTTON=(By.XPATH,"//button[contains(text(),'Next') and @type='submit']")
    CLICK_CONFIRM_BUTTON= (By.XPATH,"//button[contains(text(),'Confirm') and @type='submit']")
    PAYMENT_METHOD_BUTTON = (By.XPATH, "//div[contains(@class, 'payment')]")
    ADDING_CARD_FIELD =(By.XPATH,"//div[contains(text(),'Add card')]")
    CLICK_ADD_CARD = (By.XPATH, "//div[@class='pp-plus-container']")
    CARD_INPUT = (By.CLASS_NAME,"card_input")
    ENTER_VALID_CARD_NUMBER=(By.ID,'number')
    ENTER_CARD_CVV=(By.ID,"code")
    LINK_BUTTON=(By.XPATH,"//button[contains(text(),'Link') and @type='submit']")
    ADDED_CARD_VERIFICATION = (By.XPATH, "//label[@for='card-1']//span[@class='checkmark']")
    COMMENT_INPUT_FIELD=(By.ID,'comment')
    MESSAGE_TO_DRIVER=(By.XPATH,"//input[@placeholder='Stop at the juice bar, please']")
    ORDER_BLANKET_AND_HANDKERCHIEFS=(By.XPATH,"//div[text()='Blanket and handkerchiefs']")
    BLANKET_AND_HANDKERCHIEFS_SLIDER=(By.XPATH,"//span[@class='slider round']")
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
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable(self.CALL_TAXI_BUTTON))
        button.click()

    def get_from_address(self):
            # Return the value from the "From" field
        return self.driver.find_element(*self.FROM_FIELD).get_porperty('value')

    def get_to_address(self):
            # Return the value from the "To" field
        return self.driver.find_element(*self.TO_FIELD).get_property('value')

    def select_supportive_plan(self):
        supportive_button =self.driver.find_elements(*self.SUPPORTIVE_PLAN_ACTIVE_LOCATOR)
        class_value =supportive_button.get_attribute("class")

        if "active" in class_value:
            print("Supportive Plan is already selected")
            pass
        else:
            supportive_button.click()

        selected_button = self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR).get_attribute("class")
        class_value = selected_button.get_property("className")
        return class_value

    def get_current_selected_plan(self):
        return self.driver.find_element(*self.SUPPORTIVE_PLAN_ACTIVE_LOCATOR).get_attrobute("class")

    def get_supportive_plan_status(self):
        return self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR).get_attribute("class")

    def open_phone_field(self):
        self.wait.until(EC.element_to_be_clickable(self.OPEN_PHONE_FIELD)).click()

    def fill_phone_number(self):
        phone_input = self.wait.until(EC.visibility_of_element_located(self.PHONE_NUMBER_INPUT))
        phone_input.clear()
        phone_input.send_keys(data.PHONE_NUMBER)
        return phone_input

    def enter_sms_code(self,code):
        sms_code_input = self.wait.until(EC.visibility_of_element_located(self.PHONE_SMS_FIELD))
        sms_code_input.clear()
        sms_code_input.send_keys(code)
        return sms_code_input

    def click_next_button(self)->None:
        self.wait.until(EC.element_to_be_clickable(self.CLICK_NEXT_BUTTON)).click()


    def click_confirm_button(self)->None:
        self.wait.until(EC.element_to_be_clickable(self.CLICK_CONFIRM_BUTTON)).click()


    def get_phone_number(self):
        self.driver.find_element(*self.PHONE_FIELD).get_attribute("value")

    def add_card_and_get_method(self,number:str,code:str)->str:
        wait = WebDriverWait(self.driver, 15)

        # 1) Enter addresses
        wait.until(EC.visibility_of_element_located(self.FROM_FIELD)).clear()
        self.driver.find_element(*self.FROM_FIELD).send_keys(data.ADDRESS_FROM)

        wait.until(EC.visibility_of_element_located(self.TO_FIELD)).clear()
        self.driver.find_element(*self.TO_FIELD).send_keys(data.ADDRESS_TO)

        # 2) Call taxi
        wait.until(EC.element_to_be_clickable(self.CALL_TAXI_BUTTON)).click()

        # Select payment method
        wait.until(EC.element_to_be_clickable(self.PAYMENT_METHOD_BUTTON)).click()
        # Click add card
        wait.until(EC.element_to_be_clickable(self.ADDING_CARD_FIELD)).click()
        # Enter card number
        wait.until(EC.element_to_be_clickable(self.ENTER_VALID_CARD_NUMBER)).send_keys(number)
        # Enter CVV number
        cvv_element = wait.until(EC.presence_of_element_located(self.ENTER_CARD_CVV))
        cvv_element.send_keys(code)
        cvv_element.send_keys(Keys.TAB)
        # Click Link button
        wait.until(EC.element_to_be_clickable(self.LINK_BUTTON)).click()
        # Return the payment method text to validate
        return wait.until(EC.element_to_be_clickable(self.PAYMENT_METHOD_BUTTON)).text


    def comment_for_driver(self,message):

        comment_field = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.COMMENT_INPUT_FIELD)
        )

        # Clear any existing text (good practice) and enter message
        comment_field.clear()
        comment_field.send_keys(message)
        return comment_field.get_attribute("value")


    def order_blanket_and_handkerchiefs(self):
       slider = WebDriverWait(self.driver, 10).until(
         EC.element_to_be_clickable(self.BLANKET_AND_HANDKERCHIEFS_SLIDER)
       )
       slider.click()
       return slider.get_property("checked")

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
        self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR ).click()
        self.driver.find_element(*self.PHONE_FIELD).click()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(number)
        self.driver.find_element(*self.CLICK_NEXT_BUTTON).click()
        time.sleep(60)
        from helpers import retrieve_phone_code
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.PHONE_SMS_FIELD).send_keys(code)
        self.driver.find_element(*self.CLICK_CONFIRM_BUTTON).click()
        self.driver.find_element(*self.MESSAGE_TO_DRIVER).send_keys(message)
        self.driver.find_element(*self.CLICK_ORDER).click()
        time.sleep(60)
        self.driver.find_element(*self.MODAL_LOCATOR)







