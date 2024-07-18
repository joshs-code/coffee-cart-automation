from pages.Shop import Shop
import pytest


@pytest.mark.usefixtures("test_setup")
class TestCheckout:

    def test_product_selection(self):
        driver = self.driver
        sp = Shop(driver)
        sp.click_cafe_latte()
        sp.click_total_btn()
