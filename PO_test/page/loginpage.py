#coding=utf-8
from base.base_method import BaseMethod
from base.read_config import ReadConfig

class LoginPage():

    def __init__(self,driver):
        self.driver = driver
        self.config = ReadConfig('LocalElement.ini')
        self.base = BaseMethod(self.driver)

    def send_username(self,username):
        return self.base.find_ele('id','userameInput').send_keys(username)

    def send_password(self,userpwd):
        return self.base.find_ele('id','passwordInput').send_keys(userpwd)

    def login_click(self):
        return self.base.find_ele('id','loginSubmit').click()

    def get_loginerror_info(self):
        if self.base.find_ele('xpath','//*[@id="loginForm"]/div[3]/div[6]'):
            return self.base.get_eletext('xpath', '//*[@id="loginForm"]/div[3]/div[6]')
        else:
            return None

    def login_in(self):
        self.base.start_chrome()
        self.send_username('wangkaige')
        self.send_password('aaa111')
        self.login_click()




if __name__ == '__main__':
    pass

