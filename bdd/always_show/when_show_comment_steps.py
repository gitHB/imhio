from pytest_bdd import given, when, then
import allure


@then("окно комментария должно появиться")
def show_window(app):
    with allure.step("then окно комментария должно появиться"):
        app.fw.is_visible(must_be_visible=True)


@then("окно комментария не должно появиться")
def show_window(app):
    with allure.step("then окно комментария не должно появиться"):
        app.fw.is_visible(must_be_visible=False)
