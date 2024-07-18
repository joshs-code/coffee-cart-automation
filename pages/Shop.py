import pytest
from selenium.webdriver.common.by import By


class Shop:

    def __init__(self, driver):
        self.driver = driver
        self.cafe_latte_product_xpath = '//div[@data-test="Cafe_Latte"]'
        self.total_button_xpath = '//button[@data-test="checkout"]'

    def click_cafe_latte(self):
        self.driver.find_element(By.XPATH, self.cafe_latte_product_xpath).click()

    def click_total_btn(self):
        self.driver.find_element(By.XPATH, self.total_button_xpath).click()
