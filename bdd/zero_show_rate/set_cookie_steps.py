from pytest_bdd import given, when, then
import allure


@allure.step("Given вероятность появления окна = 0")
@given("вероятность появления окна = 0")
def zero_show_rate():
    pass


@when("удалить все cookie")
def del_cookies(app):
    with allure.step("When удалить все cookie"):
        app.common.del_cookie()


@when("обновить страницу")
def del_cookies(app):
    with allure.step("When обновить страницу"):
        app.common.refresh_page()


@then("окно не должно появиться")
def do_not_show_window(app):
    with allure.step("then окно не должно появиться"):
        app.mw.is_visible(must_be_visible=False)


@then("cookie должен появиться")
def cookie_must_be(app):
    with allure.step("then cookie должен появиться"):
        app.common.check_cookie()
