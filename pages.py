import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUrbanRoutes:

    FROM_FIELD= (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    CUSTOM_OPTION = ( By.XPATH, "//div[text()='Custom'}")
    CALL_TAXI_BUTTON = (By.XPATH,"//button[contains(text(), 'Call a taxi')]")
    SUPPORTIVE_PLAN = (By.XPATH, "//div[contains(text(),'Supportive')]")
    PHONE_NUMBER_FIELD= (By.ID,"phone")
    CLICK_next_button =(By.XPATH,"//button[contains(text(),'Next') and @type='submit']")
    CODE_INPUT_FIELD =(By.XPATH,"//input[@placeholder='xxxx']")
    CLICK_CONFIRM_BUTTON= (By.XPATH,"//button[contains(text(),'Confirm') and @type='submit')]")

    PAYMENT_METHOD = (By.XPATH, " //div[contains(text(),'Payment method')]")
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

