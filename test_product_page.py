import time

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.parametrize("number", [0, 1, 2, 3, 4, 5, 6,
                                    pytest.param(7, marks=pytest.mark.xfail),
                                    8, 9])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, number):
    link = ("http://selenium1py.pythonanywhere.com/catalogue/"
            f"coders-at-work_207/?promo=offer{number}")
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_correct_product_name_in_success_message()
    page.should_be_basket_total_equals_book_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.element_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page (browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket = BasketPage(browser, browser.current_url)
    basket.basket_is_empty()
    basket.no_item_list_in_basket()


class TestUserAddToBasketFromProductPage:


    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(
            browser,
            "http://selenium1py.pythonanywhere.com/accounts/login/"
        )
        page.open()
        email = str(time.time()) + "@gmail.com"
        password = '80808011aDf13'
        page.register_new_user(email, password)
        page.user_login_to_account()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.user_add_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()
