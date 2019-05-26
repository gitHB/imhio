@always_show @add_to_db
Feature: Проверка добавления записей в БД
  
    Scenario Outline: Проверка добавления записи без комментария
        Given вероятность появления окна = 1
        When открыть главную страницу для <user_agent>
        And удалить все cookie
        And обновить страницу
        And очистить таблицу в БД
        And выбрать в появившемся окне вариант <user_action> для: <user_agent>
        Then убедиться в добавлении соответствующей записи для <user_agent> и <user_action>
      Examples:
        | user_agent | user_action |
        | desktop    | 9           |
        | mobile     | 9           |


    Scenario Outline: Проверка добавления записи с комментарием
        Given вероятность появления окна = 1
        When открыть главную страницу для <user_agent>
        And удалить все cookie
        And обновить страницу
        And выбрать в появившемся окне вариант <user_action> для: <user_agent>
        And заполнить комментарий
        And в окне комментария нажать send
        Then убедиться в добавлении соответствующей записи для <user_agent> и <user_action>
      Examples:
        | user_agent | user_action |
        | desktop    | 2           |
        | mobile     | 2           |


    Scenario Outline: Проверка добавления записи с пустым комментарием
        Given вероятность появления окна = 1
        When открыть главную страницу для <user_agent>
        And удалить все cookie
        And обновить страницу
        And выбрать в появившемся окне вариант <user_action> для: <user_agent>
        And в окне комментария нажать send
        Then убедиться в добавлении соответствующей записи для <user_agent> и <user_action>
      Examples:
        | user_agent | user_action |
        | desktop    | 1           |
        | mobile     | 1           |