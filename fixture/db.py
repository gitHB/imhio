import random

import psycopg2
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


__author__ = 'ikozhevnikov'

"""
Методы хелперы для работы с таблицей БД
"""


class DBHelper:

    def __init__(self, app):
        self.app = app

    def execute_sql(self, execute='truncate'):
        con = None
        res = None
        sql_str = None
        connect_sql = "host='localhost' port=5433 dbname='core' user='postgres' password='devpass'"
        if execute == 'truncate':
            sql_str = "TRUNCATE public.t_feedback_models"
        if execute == 'select':
            sql_str = "SELECT * FROM public.t_feedback_models WHERE id=1 "
        if not sql_str:
            assert False, "Не задан варант запроса к БД"
        try:
            con = psycopg2.connect(connect_sql)
            cur = con.cursor()
            res = cur.execute(sql_str)
            con.commit()
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            assert False, 'Error %s' % e
        finally:
            if con:
                con.close()
        return res
