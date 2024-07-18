from selenium.webdriver.common.by import By


class PaymentDetails:

    def __init__(self, driver):
        self.driver = driver
        self.payment_title_xpath = '//h1[contains(text(), "Payment details")]'
        self.name_input_xpath = '//input[@name="name"]'
        self.email_input_xpath = '//input[@name="email"]'
        self.submit_xpath = '//button[@type="submit"]'

    def verify_payment_page(self):
        title = self.driver.find_element(By.XPATH, self.payment_title_xpath).text
        assert title == "Payment details"

    def enter_name(self, name):
        self.driver.find_element(By.XPATH, self.name_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.name_input_xpath).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_input_xpath).send_keys(email)

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.submit_xpath).click()
