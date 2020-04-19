#coding=utf-8
from selenium.webdriver.support.select import Select
from base.base_method import BaseMethod
import time


class ReservePage():

    def __init__(self,driver):
        self.driver = driver
        self.base = BaseMethod(self.driver)

    #取消保存乘客的默认候选
    def cancel_savepassenger(self):
        self.base.wait_title('机票下单页')
        xpathvalue = '//*[@id="AddEditForm"]/div[1]/div[2]/div[1]/div[3]/div/div[2]/div[2]/label/span'
        self.base.find_ele('xpath',xpathvalue).click()
        time.sleep(2)

    #输入乘客姓名
    def send_passanger(self,p_name):
        ele_xpath = '//*[@id="AddEditForm"]/div[1]/div[2]/div[1]/div[3]/div/div[2]/div[1]/input[1]'
        self.base.find_ele('xpath',ele_xpath).send_keys(p_name)

    #选择乘客证件类型并输入证件号码
    def choose_cert(self,cert_id,cert_num):
        certtype_xpath = '//*[@id="AddEditForm"]/div[1]/div[2]/div[1]/div[3]/div/div[4]/div/div[1]/select'
        element = self.base.find_ele('xpath',certtype_xpath)
        Select(element).select_by_index(cert_id)
        cert_xpath = '//*[@id="AddEditForm"]/div[1]/div[2]/div[1]/div[3]/div/div[4]/div/div[2]/input[1]'
        self.base.find_ele('xpath',cert_xpath).send_keys(cert_num)

    #填写乘机人手机号
    def write_phone(self,phone):
        ele_xpath = '//*[@id="AddEditForm"]/div[1]/div[2]/div[1]/div[3]/div/div[5]/div/input'
        self.base.find_ele('xpath', ele_xpath).send_keys(phone)

    #取消乘机人的出票短信发送
    def cancel_issuemessage(self):
        xpath_value = '//*[@id="AddEditForm"]/div[1]/div[2]/div[1]/div[3]/div/div[12]/div[1]/label[2]/span'
        self.base.move_screen('xpath',xpath_value)
        self.base.find_ele('xpath',xpath_value).click()

    #选择联系人信息为同订票人，并取消出票短信发送
    def contack_info(self):
        xpath_value = '//*[@id="AddEditForm"]/div[1]/div[2]/div[2]/div[2]/label[2]/span'
        self.base.find_ele('xpath',xpath_value).click()
        xpath_value2 = '//*[@id="AddEditForm"]/div[1]/div[2]/div[2]/div[3]/div[4]/label[2]/span'
        self.base.find_ele('xpath',xpath_value2).click()

    #点击预定
    def submit_book(self):
        xpath_value = '//*[@id="AddEditForm"]/div[1]/div[2]/div[4]/div[2]/input[2]'
        self.base.move_screen('xpath',xpath_value)
        self.base.find_ele('xpath',xpath_value).click()


    def backstage_reserve_ticket(self,p_name,cert_id,cert_num,phone):
        self.cancel_savepassenger()
        self.send_passanger(p_name)
        self.choose_cert(cert_id,cert_num)
        self.write_phone(phone)
        self.cancel_issuemessage()
        self.contack_info()
        self.submit_book()


