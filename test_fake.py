from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_сhecking_for_a_button(browser):
    browser.get(link)
    button = browser.find_elements(
        By.XPATH,
        '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]'
    )
    if not button:
        assert button, (
            'The button is missing, check if the element search selector is correct'
        )
