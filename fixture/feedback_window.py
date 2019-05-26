import random
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


__author__ = 'ikozhevnikov'

"""
Методы хелперы для работы с окном комментария
"""


class FeedbackWindowHelper:

    def __init__(self, app):
        self.app = app

    def is_visible(self, must_be_visible=True):
        wd = self.app.wd
        wait = WebDriverWait(wd, 3)
        class_name = "NPS__feedback-title"
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
            self.app.get_screenshot("feedback_window_not_visible_err")
            assert False, "Не открылось окно комментария, а должно было, см.скриншот: feedback_window_not_visible_err"
        if not must_be_visible and visible:
            self.app.get_screenshot("feedback_window_visible_err")
            assert False, "Открылось окно комментария, а не должно было, см.скриншот: feedback_window_visible_err"
        return visible

    def close(self):
        if self.is_visible():
            self.app.wd.find_element_by_class_name("NPS__close").click()

    def click_send(self):
        xpath = ".//button[.='SEND']"
        if self.is_visible():
            self.app.wd.find_element_by_xpath(xpath).click()

    def input_feedback(self, text='Lorem ipsum test'):
        if self.is_visible():
            wd = self.app.wd
            text_area = wd.find_element_by_id('feedbackTextarea')
            for char in text:
                text_area.send_keys(char)
                time.sleep(0.1)
