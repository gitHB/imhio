@always_show @set_cookie
Feature: Проверка установки cookie
  
    Scenario: Проверка установки cookie с отображением окна и закрытием
        Given вероятность появления окна = 1
        When открыть главную страницу
        And удалить все cookie
        And обновить страницу
        And закрыть окно нажав на крестик
        Then cookie должен появиться
    
    
    Scenario Outline: Проверка установки cookie с отображением окна и выбором вероятности
        Given вероятность появления окна = 1
        When открыть главную страницу
        And удалить все cookie
        And обновить страницу
        And выбрать в появившемся окне вариант <user_action> для: <user_agent>
        Then cookie должен появиться
        Examples:
            | user_action | user_agent |
            | 10          | desktop    |


    Scenario Outline: Проверка установки cookie с отображением окна и закрытием окна комментария
        Given вероятность появления окна = 1
        When открыть главную страницу
        And удалить все cookie
        And обновить страницу
        And выбрать в появившемся окне вариант <user_action> для: <user_agent>
        And закрыть окно комментария
        Then cookie должен появиться
        Examples:
            | user_action | user_agent |
            | 0           | desktop    |


    Scenario Outline: Проверка установки cookie с отображением окна и отправкой с пустым комментарием
        Given вероятность появления окна = 1
        When открыть главную страницу
        And удалить все cookie
        And обновить страницу
        And выбрать в появившемся окне вариант <user_action> для: <user_agent>
        And в окне комментария нажать send
        Then cookie должен появиться
        Examples:
            | user_action | user_agent |
            | 0           | desktop    |


    Scenario Outline: Проверка установки cookie с отображением окна и отправкой с комментарием
        Given вероятность появления окна = 1
        When открыть главную страницу
        And удалить все cookie
        And обновить страницу
        And выбрать в появившемся окне вариант <user_action> для: <user_agent>
        And заполнить комментарий
        And в окне комментария нажать send
        Then cookie должен появиться
        Examples:
            | user_action | user_agent |
            | 0           | desktop    |
