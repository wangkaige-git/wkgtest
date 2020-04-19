#coding=utf-8
from selenium import webdriver
import time
import unittest
from base.base_method import BaseMethod
from page.loginpage import LoginPage
from base.read_excel import ReadExcel
from ddt import ddt,data
from log.user_log import UserLog
excel_data = ReadExcel()
testdata = excel_data.get_data()

@ddt
class Logincase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        web_driver = webdriver.Chrome()
        self.base_m = BaseMethod(web_driver)
        self.driver = self.base_m.start_chrome()
        self.login_p = LoginPage(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def tearDown(self):
        self.driver.close()

    #登陆
    @unittest.skip("用户名密码都为空用例不执行")
    @data(*testdata)
    def test_login(self,testdata):
        username,userpwd,error_info = testdata
        self.login_p.send_username(username)
        self.login_p.send_password(userpwd)
        self.login_p.login_click()
        time.sleep(1)
        errorcode = self.login_p.get_loginerror_info()
        print (errorcode)
        return self.assertEqual(errorcode,error_info)


if __name__ == '__main__':
    pass




