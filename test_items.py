website_link = "http://selenium1py.pythonanywhere.com"
search_input_locator = "id_q"
search_button_locator = "div.navbar-collapse.primary-collapse.collapse > form > input"
add_button_name_locator = "div.product_price > form > button"


# 3. Book search
def test_book_search(browser):

    #Data
    search_text = "The shellcoder's handbook"
    add_button_name = "Añadir al carrito"

    # Arrange
    browser.get(website_link)

    # Act
    search_input = browser.find_element_by_id(search_input_locator)
    search_input.clear()
    search_input.send_keys(search_text)
    search_button = browser.find_element_by_css_selector(search_button_locator)
    search_button.click()

    # Assert
    add_button_name_text = browser.find_element_by_css_selector(add_button_name_locator)
    assert add_button_name in add_button_name_text.text, "Book not found" % (add_button_name_text, add_button_name)
