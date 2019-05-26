import pytest
from pytest_bdd import scenario
from .smoke.open_main_page_steps import *
from .zero_show_rate.set_cookie_steps import *
from .always_show.set_cookie_steps import *
from .always_show.when_show_steps import *
from .always_show.when_show_comment_steps import *
from .always_show.add_to_db_steps import *


@pytest.mark.blocker
@scenario('smoke/open_main_page.feature', 'Тест открытия главной страницы')
def test_open_main_page_scenario():
    pass


# @scenario('zero_show_rate/set_cookie.feature', 'Проверка вероятности появления окна без установленной cookie')
# def test_show_window_without_cookie_scenario():
#     pass
#
#
# @scenario('zero_show_rate/set_cookie.feature', 'Проверка установки cookie без отображения окна')
# def test_set_cookie_without_show_window_scenario():
#     pass


@scenario('always_show/set_cookie.feature', 'Проверка установки cookie с отображением окна и закрытием')
def test_set_cookie_with_show_window_and_close_scenario():
    pass


@scenario('always_show/set_cookie.feature', 'Проверка установки cookie с отображением окна и выбором вероятности')
def test_set_cookie_with_show_window_and_user_action_scenario():
    pass


@scenario('always_show/set_cookie.feature', 'Проверка установки cookie с отображением окна и закрытием окна комментария')
def test_set_cookie_with_show_feedback_window_and_close_scenario():
    pass


@scenario('always_show/set_cookie.feature', 'Проверка установки cookie с отображением окна и отправкой с пустым комментарием')
def test_set_cookie_with_empty_feedback_scenario():
    pass


@scenario('always_show/set_cookie.feature', 'Проверка установки cookie с отображением окна и отправкой с комментарием')
def test_set_cookie_with_send_feedbac_scenario():
    pass


@scenario('always_show/when_show.feature', 'Проверка появления окна с установленной cookie')
def test_not_to_show_with_cookie_scenario():
    pass


@scenario('always_show/when_show.feature', 'Проверка появления окна без установленной cookie')
def test_show_without_cookie_scenario():
    pass


@scenario('always_show/when_show_comment.feature', 'Проверка появления окна комментария для оценок <=6')
def test_show_feedback_window_scenario():
    pass


@scenario('always_show/when_show_comment.feature', 'Проверка появления окна комментария для оценок >=7')
def test_not_to_show_feedback_window_scenario():
    pass


@scenario('always_show/add_to_db.feature', 'Проверка добавления записи без комментария')
def test_add_without_feedback_scenario():
    pass


@scenario('always_show/add_to_db.feature', 'Проверка добавления записи с комментарием')
def test_add_with_feedback_scenario():
    pass


@scenario('always_show/add_to_db.feature', 'Проверка добавления записи с пустым комментарием')
def test_add_with_empty_feedback_scenario():
    pass
