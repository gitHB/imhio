import random
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


__author__ = 'ikozhevnikov'

"""
Методы хелперы для работы с основным окном оценок
"""


class MainWindowHelper:

    def __init__(self, app):
        self.app = app

    def is_visible(self, must_be_visible=False):
        wd = self.app.wd
        wait = WebDriverWait(wd, 5)
        class_name = "NPS"
        visible = False
        if wd.find_elements_by_class_name(class_name):
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
            visible = True
        else:
            try:
                wait.until(EC.visibility_of_element_located((By.ID, class_name)))
            except TimeoutException:
                visible = False
        if must_be_visible and not visible:
            self.app.get_screenshot("main_window_not_visible_err")
            assert False, "Не открылось главное окно, а должно было, см.скриншот: main_window_not_visible_err"
        elif not must_be_visible and visible:
            self.app.get_screenshot("main_window_visible_err")
            assert False, "Открылось главное окно, а не должно было, см.скриншот: main_window_visible_err"
        return visible

    def close(self):
        if self.is_visible(must_be_visible=True):
            self.app.wd.find_element_by_class_name("NPS__close").click()

    def click_user_action(self, user_action, mode='desktop'):
        xpath = ".//div[@class='NPS__buttons']/div[.='" + user_action + "']"
        if mode == 'mobile':
            xpath = ".//div[@class='NPS__buttons--mobile']/div[.='" + user_action + "']"
        if self.is_visible(must_be_visible=True):
            self.app.wd.find_element_by_xpath(xpath).click()
