from pages.Shop import Shop
from pages.PaymentDetails import PaymentDetails
from pages.Cart import Cart
import pytest
import names


@pytest.mark.usefixtures("test_setup")
class TestCheckout:

    def test_product_scenario_1(self):
        driver = self.driver
        sp = Shop(driver)
        sp.click_cafe_latte()
        sp.click_total_btn()

        pp = PaymentDetails(driver)
        pp.verify_payment_page()
        name = names.get_first_name()
        email = names.get_first_name() + '@test.com'
        pp.enter_name(name)
        pp.enter_email(email)
        pp.click_submit()

        sp = Shop(driver)
        sp.verify_purchase()

    def test_product_scenario_2(self):
        driver = self.driver
        sp = Shop(driver)
        sp.click_mocha()
        sp.click_flat_white()
        sp.click_cart()

        cp = Cart(driver)
        cp.verify_cart()
        cp.click_total_btn()

        pp = PaymentDetails(driver)
        pp.verify_payment_page()
        name = names.get_first_name()
        email = names.get_first_name() + '@test.com'
        pp.enter_name(name)
        pp.enter_email(email)
        pp.click_submit()

        sp = Shop(driver)
        sp.verify_purchase()

