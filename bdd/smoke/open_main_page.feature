@smoke

    Scenario Outline: Тест открытия главной страницы
        Given веб адрес <url>
        When открыть главную страницу
        Then заголовок страницы содержит <title>
        Examples: Vertical
        | url   | http://localhost:58001/ |
        | title | NPS Example             |