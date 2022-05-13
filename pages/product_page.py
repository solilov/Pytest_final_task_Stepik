from .base_page import BasePage
from .locators import ProductPageLocators as Locators


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*Locators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def user_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(
            *Locators.ADD_TO_BASKET_BUTTON
        )
        button_add_to_basket.click()

    def should_be_correct_product_name_in_success_message(self):
        expected = self.browser.find_element(*Locators.BOOK_TITLE).text
        actual = self.browser.find_element(*Locators.ADDED_BOOK_TITLE).text
        message = f'Wrong book title: expected "{expected}", got "{actual}"'
        assert actual == expected, message

    def should_be_basket_total_equals_book_price(self):
        price = self.browser.find_element(*Locators.BOOK_PRICE).text
        basket_total = self.browser.find_element(*Locators.BASKET_TOTAL).text
        message = f'Wrong basket total: expected "{price}", got "{basket_total}"'
        assert basket_total == price, message

    def should_be_message_about_adding(self):
        assert self.is_element_present(
            *Locators.BOOK_TITLE
        ), "Product name is not presented"
        assert self.is_element_present(
            *Locators.ADDED_BOOK_TITLE
        ), "Message about adding is not presented"
        book_title = self.browser.find_element(*Locators.BOOK_TITLE).text
        message = self.browser.find_element(*Locators.ADDED_BOOK_TITLE).text
        assert book_title == message, "Book title is wrong in the message"

    def should_be_message_basket_total(self):
        assert self.is_element_present(
            *Locators.BASKET_TOTAL
        ), "Message basket total is not presented"
        assert self.is_element_present(
            *Locators.BOOK_PRICE
        ), "Product price is not presented"
        basket_total = self.browser.find_element(
            *Locators.BASKET_TOTAL
        ).text
        book_price = self.browser.find_element(*Locators.BOOK_PRICE).text
        assert book_price == basket_total, "Price is wrong in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *Locators.ADDED_BOOK_TITLE
        ), "Success message is presented, but should not be"

    def element_disappeared(self):
        assert self.is_disappeared(
            *Locators.ADDED_BOOK_TITLE
        ), "Element did not disappear"
