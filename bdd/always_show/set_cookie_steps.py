from pytest_bdd import given, when, then
import allure


@allure.step("Given вероятность появления окна = 1")
@given("вероятность появления окна = 1")
def allways_show_rate():
    pass


@when("закрыть окно нажав на крестик")
def close_main_window(app):
    with allure.step("When закрыть окно нажав на крестик"):
        app.mw.close()


@when("выбрать в появившемся окне вариант <user_action> для: <user_agent>")
def click_user_action(app, user_action, user_agent):
    with allure.step("When выбрать в появившемся окне вариант <user_action> для: <user_agent>"):
        app.mw.click_user_action(user_action, mode=user_agent)


@when("закрыть окно комментария")
def close_feedback_window(app):
    with allure.step("When закрыть окно комментария"):
        app.fw.close()


@when("в окне комментария нажать send")
def click_send(app):
    with allure.step("When в окне комментария нажать send"):
        app.fw.click_send()


@when("заполнить комментарий")
def input_feedback_window(app):
    with allure.step("When заполнить комментарий"):
        app.fw.input_feedback()
