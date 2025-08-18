import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    FROM_FIELD= (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    CUSTOM_OPTION = ( By.XPATH, "//div[text()='Custom'}")
    CALL_TAXI_BUTTON = (By.XPATH,"//button[contains(text(), 'Call a taxi')]")
    SUPPORTIVE_PLAN_ACTIVE_LOCATOR = (By.XPATH, "//button[@data-for='tariff-card-4' and contains(@class, 'active')]")
    SUPPORTIVE_PLAN_LOCATOR = (By.XPATH, "//button[@data-for='tariff-card-4']")
    PHONE_NUMBER_FIELD= (By.ID,"phone")
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
    MESSAGE_TO_DRIVER=(By.XPATH,"//input[@placeholder='Get some whiskey']")
    ORDER_BLANKET_AND_HANDKERCHIEFS=(By.XPATH,"//div[text()='Blanket and handkerchiefs']")
    BLANKET_AND_HANDKERCHIEFS_SLIDER=(By.XPATH,"//span[@class='slider round']")
    ICE_SCREAMS_BUCKET=(By.XPATH,"//div[contains(text(),'Ice screams')]")
    ORDER_2_ICE_CREAMS=(By.XPATH, "//div[contains(@class, 'counter-plus')]")



    def set_from_address(self,address):
        self.driver.find_element(*self.FROM_FIELD).send_keys(address)
    def set_to_address(self,address):
        self.driver.find_element(*self.TO_FIELD).send_keys(address)
    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()

    def select_supportive_plan(self):

        active_elements = self.driver.find_elements(*SUPPORTIVE_PLAN_ACTIVE_LOCATOR)

        if active_elements:
            print("SUpportive Plan is already selected")
            pass
        else:
            supportive_button = self.driver.find_element(*SUPPORTIVE_PLAN_LOCATOR)
            supportive_button.click()

        selected_button = self.driver.find_element(*SUPPORTIVE_PLAN_LOCATOR)
        class_value = selected_button.get_property("className")
        assert "active" in class_value, f"Supportive plan is not selected. Class: (class_value)"
        button_text = selected_button.text

        assert "Supportive" in button_text, f"Expected 'Supportive' in button text, got: (button_text)"

