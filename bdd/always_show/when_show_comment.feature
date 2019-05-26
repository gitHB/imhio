@always_show @when_show_comment
Feature: Проверка условий отображения окна комментария

    Scenario Outline: Проверка появления окна комментария для оценок <=6
        Given вероятность появления окна = 1
        When открыть главную страницу
        And удалить все cookie
        And обновить страницу
        And выбрать в появившемся окне вариант <user_action> для: <user_agent>
        Then окно комментария должно появиться
        Examples:
            | user_action | user_agent |
            | 0           | desktop    |
            | 1           | desktop    |
            | 5           | desktop    |
            | 6           | desktop    |


    Scenario Outline: Проверка появления окна комментария для оценок >=7
        Given вероятность появления окна = 1
        When открыть главную страницу
        And удалить все cookie
        And обновить страницу
        And выбрать в появившемся окне вариант <user_action> для: <user_agent>
        Then окно комментария не должно появиться
        Examples:
            | user_action | user_agent |
            | 7           | desktop    |
            | 8           | desktop    |
            | 9           | desktop    |
            | 10          | desktop    |