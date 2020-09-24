from selenium import webdriver
import random
import pytest

website_link = "http://selenium1py.pythonanywhere.com/ru/"
success_message_locator = "alertinner"
sign_in_locator = "login_link"
sign_up_email_input_locator = "id_registration-email"
sign_up_password_input_locator = "id_registration-password1"
confirm_sign_up_password_input_locator = "id_registration-password2"
password_1 = "karandash123"
sign_up_submit_locator = "registration_submit"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

# 1. Registration
def test_sign_up(browser):
    domen = ""
    email = ""
    for x in range(12):
        domen = domen + random.choice(list("1234567890qwertyuiopasdfghjklzxcvbnm"))
        email = domen + "@" + "mail.ru"
    print(email)

    # Data
    success_sigh_up_message = "Спасибо за регистрацию!"

    # Arrange
    browser.get(website_link)

    # Act
    sigh_up_button = browser.find_element_by_id(sign_in_locator)
    sigh_up_button.click()
    email_input = browser.find_element_by_id(sign_up_email_input_locator)
    email_input.send_keys(email)
    password_input = browser.find_element_by_id(sign_up_password_input_locator)
    password_input.send_keys(password_1)
    confirm_password_input = browser.find_element_by_id(confirm_sign_up_password_input_locator)
    confirm_password_input.send_keys(password_1)
    confirm_registration_button = browser.find_element_by_name(sign_up_submit_locator)
    confirm_registration_button.click()

    # Assert
    success_message = browser.find_element_by_class_name(success_message_locator)
    assert success_sigh_up_message in success_message.text, \
        "Sign up page should contain valid success message" % (success_message, success_sigh_up_message)
