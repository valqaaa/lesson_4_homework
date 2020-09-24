import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default=None,
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")


    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})

    print("\nstart browser for test..")
    option = webdriver.Chrome(options=options)
    option.implicitly_wait(5)

    yield option

    print("\nquit browser..")
    option.quit()
