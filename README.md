Ivan Kozhevnikov hansb@yandex.ru 
=================================

Python 3+ PyTest Pytest-BDD Selenium 3+

QUICK START
-----------
**>py.test --alluredir allure-reports --browser chrome --base_url http://localhost:58001/ bdd\main_scenarios.py**

*--alluredir: path to store allure report    
*--browser: ie, chrome (by default), firefox  
*--base_url: http://localhost:58001/ default value  
*bdd\main_scenarios.py: main test scenarios

DOCKER
------
to build standalone container with tests use Dockerfile: 
>docker build --tag="imhio"

to run tests with selenium-chrome container use docker-compose.yml
>docker-compose up

ALLURE LOG
----------
to generate allure log after test run use:
>allure generate