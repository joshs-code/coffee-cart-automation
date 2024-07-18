import pytest
from selenium.webdriver.common.by import By
import time

class Shop:

    def __init__(self, driver):
        self.driver = driver
        self.cafe_latte_product_xpath = '//div[@data-test="Cafe_Latte"]'
        self.total_button_xpath = '//button[@data-test="checkout"]'
        self.verify_payment_text_xpath = '//div[contains(text(), "Thanks for your purchase. Please check your email for payment.")]'

    def click_cafe_latte(self):
        self.driver.find_element(By.XPATH, self.cafe_latte_product_xpath).click()

    def click_total_btn(self):
        self.driver.find_element(By.XPATH, self.total_button_xpath).click()

    def verify_purchase(self):
        time.sleep(2)
        purchase_text = self.driver.find_element(By.XPATH, self.verify_payment_text_xpath).text
        print(purchase_text)
        assert purchase_text == "Thanks for your purchase. Please check your email for payment."