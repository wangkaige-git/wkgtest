#coding=utf-8
from selenium import webdriver
import unittest
from base.base_method import BaseMethod
from page.loginpage import LoginPage
from page.home_page import HomePage
from page.reserve_page import ReservePage
from log.user_log import UserLog

class Logincase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        global web_driver
        web_driver = webdriver.Chrome()
        self.base_m = BaseMethod(web_driver)
        self.driver = self.base_m.start_chrome()
        self.login_p = LoginPage(self.driver)
        self.login_p.login_in()
        self.home_p = HomePage(self.driver)
        self.reserve_p = ReservePage(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def tearDown(self):
        pass
        #self.driver.close()

    def test_backstate_book_ticket(self):
        self.home_p.backstate_search('王凯歌测试','杭州','北京','2020-04-20')
        self.home_p.more_carbin()
        self.home_p.choose_carbin()
        self.reserve_p.backstage_reserve_ticket('葫芦娃',2,'huluwa',15809283436)





    if __name__ == '__main__':
        pass
