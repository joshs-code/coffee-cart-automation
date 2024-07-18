from pages.Shop import Shop
from pages.PaymentDetails import PaymentDetails
import pytest
import names


@pytest.mark.usefixtures("test_setup")
class TestCheckout:

    def test_product_selection(self):
        driver = self.driver
        sp = Shop(driver)
        sp.click_cafe_latte()
        sp.click_total_btn()

    def test_payment(self):
        driver = self.driver
        pp = PaymentDetails(driver)
        pp.verify_payment_page()
        name = names.get_first_name()
        email = names.get_first_name() + '@test.com'
        pp.enter_name(name)
        pp.enter_email(email)
        pp.click_submit()

    def test_confirm_purchase(self):
        driver = self.driver
        sp = Shop(driver)
        sp.verify_purchase()