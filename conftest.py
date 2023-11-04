import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

lang_list = ['ru', 'en', 'fr', 'it', 'es']


def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='ru',
        help='Choose user language in browser: ru, en, fr, etc'
    )


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")  # Извлечение параметра language
    if language in lang_list:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)  # Запуск браузера с установленными опциями
    else:
        browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
