import sys
import time
import urllib.request
from urllib.error import URLError

import pytest
from fixture.application import Application


__author__ = 'ikozhevnikov'

"""
Общие фикстуры для всех тестовых методов
"""

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    docker_adr = request.config.getoption("--docker_adr")
    attempt = 0
    resp = None
    if docker_adr:
        while True:
            attempt += 1
            try:
                resp = urllib.request.urlopen(docker_adr)
            except URLError:
                pass
            if resp:
                break
            if attempt > 5:
                sys.exit("No response from docker_adr: " + str(docker_adr))
            time.sleep(4)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=base_url, docker_adr=docker_adr)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        if fixture:
            fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--base_url", action="store", default="http://localhost:58001")
    parser.addoption("--docker_adr", action="store", default="")

