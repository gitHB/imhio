import allure
from pytest_bdd import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@allure.step("Given веб адрес {url}")
@given("веб адрес <url>")
def given_url(url):
    return url


@when("открыть главную страницу")
def open_page(app):
    with allure.step("When открыть главную страницу"):
        app.open_home_page()


@when("открыть заданную страницу <url>")
def open_page(app, url):
    with allure.step("When открыть заданную страницу {url}"):
        app.open_url(url)


# Все тестовые методы вынесены в соответствующие файлы, но для такого простого, нет смысла описывать отдельный метод
# Все же, моветон работать с вебдрайвером сразу в steps, не делайте так
@then("заголовок страницы содержит <title>")
def title_contains(app, title):
    with allure.step("Then заголовок страницы содержит {title"):
        wd = app.wd
        wait = WebDriverWait(wd, 20)
        wait.until(EC.title_contains(title))
