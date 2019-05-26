from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
from fixture.common_fixtures import CommonHelper
from fixture.feedback_window import FeedbackWindowHelper
from fixture.main_window import MainWindowHelper
from fixture.db import DBHelper


__author__ = 'ikozhevnikov'


class Application:
    def __init__(self, browser, base_url, docker_adr):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            if docker_adr is "":
                self.wd = webdriver.Chrome(ChromeDriverManager().install())
            else:
                chrome_options = ChromeOptions()
                chrome_options.add_argument("--disable-dev-shm-usage")
                desired_caps = chrome_options.to_capabilities()
                desired_caps['browserName'] = 'chrome'
                self.wd = webdriver.Remote(str(docker_adr), desired_capabilities=desired_caps)
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.common = CommonHelper(self)
        self.db = DBHelper(self)
        self.mw = MainWindowHelper(self)
        self.fw = FeedbackWindowHelper(self)
        self.base_url = base_url

    def switch_to(self, mode='desktop'):
        if mode == 'desktop' and self.wd.capabilities.get('mobileEmulationEnabled'):
            self.destroy()
            self.wd = webdriver.Chrome(ChromeDriverManager().install())
        elif mode == "mobile" and not self.wd.capabilities.get('mobileEmulationEnabled'):
            self.destroy()
            mobile_emulation = {"deviceName": "Nexus 5"}
            chrome_options = ChromeOptions()
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            self.wd = webdriver.Chrome(chrome_options=chrome_options)

    def open_home_page(self):
        self.open_url(self.base_url)

    def open_url(self, url):
        wd = self.wd
        wd.get(url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def get_screenshot(self, text="screenshot"):
        allure.attach(self.wd.get_screenshot_as_png(), text, AttachmentType.PNG)
