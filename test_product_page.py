import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize("number", [0, 1, 2, 3, 4, 5, 6,
                                    pytest.param(7, marks=pytest.mark.xfail),
                                    8, 9])
def test_guest_can_add_product_to_basket(browser, number):
    link = ("http://selenium1py.pythonanywhere.com/catalogue/"
            f"coders-at-work_207/?promo=offer{number}")
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_correct_product_name_in_success_message()
    page.should_be_basket_total_equals_book_price()
