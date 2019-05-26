@zero_show_rate @set_cookie
Feature: Проверка установки cookie

    Scenario: Проверка вероятности появления окна без установленной cookie
        Given вероятность появления окна = 0
        When открыть главную страницу
        And удалить все cookie
        And обновить страницу
        Then окно не должно появиться


    Scenario: Проверка установки cookie без отображения окна
        Given вероятность появления окна = 0
        When открыть главную страницу
        And удалить все cookie
        And обновить страницу
        Then cookie должен появиться