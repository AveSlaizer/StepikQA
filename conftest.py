import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

lang_list = ['ru', 'en', 'fr', 'it', 'es']


def pytest_addoption(parser):
    parser.addoption(
        '--user_language',
        action='store',
        default='ru',
        help='Choose user language in browser: ru, en, fr, etc'
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("user_language")  # Извлечение параметра user_language
    if user_language in lang_list:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)  # Запуск браузера с установленными опциями
    else:
        browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
