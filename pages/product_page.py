from .base_page import BasePage
from .locators import ProductPageLocators as Locators


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*Locators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def should_be_correct_product_name_in_success_message(self):
        expected = self.browser.find_element(*Locators.BOOK_TITLE).text
        actual = self.browser.find_element(*Locators.ADDED_BOOK_TITLE).text
        msg = f'Wrong book title: expected "{expected}", got "{actual}"'
        assert actual == expected, msg

    def should_be_basket_total_equals_book_price(self):
        price = self.browser.find_element(*Locators.BOOK_PRICE).text
        basket_total = self.browser.find_element(*Locators.BASKET_TOTAL).text
        msg = f'Wrong basket total: expected "{price}", got "{basket_total}"'
        assert basket_total == price, msg

    def press_button_add_to_basket(self):
        # Нажимаем кнопку Add to basket
        button_add_to_basket = self.browser.find_element(*Locators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_message_about_adding(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*Locators.PRODUCT_NAME), "Product name is not presented"
        assert self.is_element_present(*Locators.MESSAGE_ABOUT_ADDING), "Message about adding is not presented"
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*Locators.PRODUCT_NAME).text
        message = self.browser.find_element(*Locators.MESSAGE_ABOUT_ADDING).text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        assert product_name == message, "Product name is wrong in the message"
        #assert product_name in message, "No product name in the message"

    def should_be_message_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*Locators.MESSAGE_BASKET_TOTAL), "Message basket total is not presented"
        assert self.is_element_present(*Locators.PRODUCT_PRICE), "Product price is not presented"
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*Locators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*Locators.PRODUCT_PRICE).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price == message_basket_total, "Price is wrong in the message"
        #assert product_price in message_basket_total, "No product price in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*Locators.MESSAGE_ABOUT_ADDING), \
            "Success message is presented, but should not be"

    def element_disappeared(self):
        assert self.is_disappeared(*Locators.MESSAGE_ABOUT_ADDING), \
            "Element did not disappear"
