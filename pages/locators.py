from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (
        By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a'
    )
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD = (By.ID, "id_registration-password1")
    CONF_PASSWORD = (By.ID, "id_registration-password2")
    BTN_REG = (By.NAME, "registration_submit")
    LOG_OUT = (By.ID, "logout_link")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ADDED_BOOK_TITLE = (By.CSS_SELECTOR, ".alert-success strong")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info strong")


class BasketPageLocators():
    TEXT_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner a")
    ITEMS_LIST = (By.CLASS_NAME, 'basket-items')
