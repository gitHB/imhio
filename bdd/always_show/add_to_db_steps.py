from pytest_bdd import given, when, then
import allure


@when("открыть главную страницу для <user_agent>")
def switch_mode(app, user_agent):
    with allure.step("When открыть главную страницу для <user_agent>"):
        app.switch_to(mode=user_agent)
        app.open_home_page()


@when("очистить таблицу в БД")
def truncate(app):
    with allure.step("When очистить таблицу в БД"):
        app.db.execute_sql(execute='truncate')


@then("убедиться в добавлении соответствующей записи для <user_agent> и <user_action>")
def select(app, user_agent, user_action):
    with allure.step("Then убедиться в добавлении соответствующей записи для <user_agent> и <user_action>"):
        app.db.execute_sql(execute='select')
