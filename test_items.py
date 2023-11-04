import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button_visible(browser):
    browser.get(link)
    basket = browser.find_elements(By.CSS_SELECTOR, 'span.btn-group > a.btn.btn-default')
    assert len(basket) == 1  # Проверяет наличие кнопки и бонусом уникальность селектора
    time.sleep(10)


"""
Команды запуска тестов:
pytest -s -v test_items.py - по умолчанию русский
pytest -s -v --language=fr test_items.py - французский
pytest -s -v --language=en test_items.py - английский
pytest -s -v --language=es test_items.py - испанский
pytest -s -v --language=ru test_items.py - французский
"""
