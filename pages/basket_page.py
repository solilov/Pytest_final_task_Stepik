from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        empty_text = self.browser.find_element(
            *BasketPageLocators.TEXT_BASKET_EMPTY
        )
        assert empty_text.text in "Continue shopping"

    def no_item_list_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.ITEMS_LIST
        ), 'Item list exists, basket is not empty'
        assert True
