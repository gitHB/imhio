
__author__ = 'ikozhevnikov'

"""
Общие методы хелперы
"""


class CommonHelper:

    def __init__(self, app):
        self.app = app

    def del_cookie(self):
        self.app.wd.delete_all_cookies()

    def set_cookie(self):
        if not self.app.wd.get_cookie("NPS_sended"):
            self.app.wd.add_cookie({'name': 'NPS_sended', 'value': '1', 'domain': 'localhost'})

    def check_cookie(self):
        if not self.app.wd.get_cookie("NPS_sended"):
            assert False, "Не найден cookie с именем NPS_sended."

    def refresh_page(self):
        self.app.wd.execute_script("location.reload(true);")
