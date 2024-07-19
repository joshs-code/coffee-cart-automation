from selenium.webdriver.common.by import By


class Cart:

    def __init__(self, driver):
        self.driver = driver
        self.flat_white_cart_xpath ='//div[contains(text(), "Flat White")]'
        self.mocha_cart_xpath = '//div[contains(text(), "Mocha")]'
        self.total_btn_xpath = '//button[@class="pay"]'


    def verify_cart(self):
        flat_white = self.driver.find_element(By.XPATH, self.flat_white_cart_xpath).text
        assert flat_white == "Flat White"

        mocha = self.driver.find_element(By.XPATH, self.mocha_cart_xpath).text
        assert mocha == "Mocha"

        self.driver.save_screenshot('./screenshots/cart.png')

    def click_total_btn(self):
        self.driver.find_element(By.XPATH, self.total_btn_xpath).click()