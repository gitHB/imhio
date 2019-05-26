from pytest_bdd import given, when, then
import allure


@when("установить cookie")
def set_cookie(app):
    with allure.step("When установить cookie"):
        app.common.set_cookie()


@then("окно должно появиться")
def show_window(app):
    with allure.step("then окно должно появиться"):
        app.mw.is_visible(must_be_visible=True)
