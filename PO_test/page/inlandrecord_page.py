# coding=utf-8
from base.base_method import BaseMethod
from selenium.webdriver.support.select import Select
import time


class InlandrecordPage():
    def __init__(self, driver):
        self.base = BaseMethod(driver)

    # 企业信息部分
    def write_company(self):
        value1 = '//*[@id="AddEditForm"]/div[2]/div[1]/div[2]/div/div[1]/div/input[1]'
        value2 = '//*[@id="AddEditForm"]/div[2]/div[1]/div[2]/div/div[1]/div/ul/li[1]'
        companyname = '王凯歌测试'
        self.base.send_and_choose('xpath', value1, 'xpath', value2, companyname)
    def write_reservation(self):
        xpath_value = '//*[@id="AddEditForm"]/div[2]/div[1]/div[2]/div/div[5]/div/div/input[1]'
        re_name = '张三'
        self.base.find_ele('xpath', xpath_value).send_keys(re_name)
    def write_pnr(self):
        xpath_value = '//*[@id="AddEditForm"]/div[2]/div[1]/div[2]/div/div[11]/div/input'
        self.base.find_ele('xpath', xpath_value).send_keys('000000')
    # 航段信息部分
    def write_cityfrom(self):
        xpath_value1 = '//*[@id="CityFromjs_1"]'
        self.base.move_screen('xpath', xpath_value1)
        xpath_value2 = '/html/body/div[11]/ul/li'
        fromcity = '杭州'
        self.base.send_and_choose('xpath', xpath_value1, 'xpath', xpath_value2, fromcity)
    def write_cityend(self):
        xpath_value1 = '//*[@id="CityEndjs_1"]'
        xpath_value2 = '/html/body/div[12]/ul/li[1]'
        endcity = '北京'
        self.base.send_and_choose('xpath', xpath_value1, 'xpath', xpath_value2, endcity)
    def write_flightno(self):
        xpath_value = '//*[@id="AddEditForm"]/div[2]/div[2]/div[2]/div/div[2]/div/input'
        self.base.find_ele('xpath', xpath_value).send_keys('CA1111')
    def write_carbin(self):
        xpath_value = '//*[@id="AddEditForm"]/div[2]/div[2]/div[2]/div/div[3]/div/input'
        self.base.find_ele('xpath', xpath_value).send_keys('V')
    def write_salecount(self):
        xpath_value = '//*[@id="AddEditForm"]/div[2]/div[2]/div[2]/div/div[4]/div/input'
        self.base.find_ele('xpath', xpath_value).click()
        time.sleep(1)
        if not self.base.find_ele('xpath', xpath_value).get_attribute('value'):
            self.base.find_ele('xpath', xpath_value).send_keys('6.00')
    def write_filghtdate(self):
        xpath_value = '//*[@id="AddEditForm"]/div[2]/div[2]/div[2]/div/div[6]/div/input'
        self.base.find_ele('xpath', xpath_value).send_keys('2020-03-09')
        # self.driver.switch_to.default_content()
    def write_starttime(self):
        xpath_value = '//*[@id="AddEditForm"]/div[2]/div[2]/div[2]/div/div[7]/div[1]/input'
        self.base.find_ele('xpath', xpath_value).send_keys('0830')
    def write_endtime(self):
        name_value = 'LandingTime_1'
        self.base.find_ele('name', name_value).send_keys('1230')
    def write_airrax(self):
        name_value = 'AirportTax_1'
        self.base.find_ele('name', name_value).send_keys('50')
    def write_fuel(self):
        name_value = 'BunkerFee_1'
        self.base.find_ele('name', name_value).send_keys('0')
    def write_totalprice(self):
        name_value = 'TotalPrice_1'
        self.base.find_ele('name', name_value).click()
        time.sleep(1)
        if not self.base.find_ele('name', name_value).get_attribute('value'):
            self.base.find_ele('name', name_value).send_keys('800')
    def write_facevalue(self):
        name_value = 'FaceValue_1'
        self.base.find_ele('name', name_value).click()
        time.sleep(1)
        if not self.base.find_ele('name', name_value).get_attribute('value'):
            self.base.find_ele('name', name_value).send_keys('800')
    def write_transferprice(self):
        name_value = 'TransferPrice_1'
        self.base.find_ele('name', name_value).send_keys('800')
    def write_buycount(self):
        name_value = 'BuyDiscount_1'
        self.base.find_ele('name', name_value).send_keys('6.00')
    # 乘机人信息部分
    def write_cname(self):
        name_value = 'PassengerChineseName_1'
        self.base.move_screen('name', name_value)
        self.base.find_ele('name', name_value).send_keys('葫芦娃')
    def choose_passagetype(self, x):
        """1是成人"""
        xpath_value = '//*[@id="AddEditForm"]/div[2]/div[3]/div[2]/div[2]/div/div[1]/div[3]/div/select'
        element = self.base.find_ele('xpath', xpath_value)
        Select(element).select_by_index(x)
    # 选择乘客证件类型并输入证件号码(2是护照)
    def choose_cert(self, x, cert_num):
        xpath_value = '//*[@id="AddEditForm"]/div[2]/div[3]/div[2]/div[2]/div/div[1]/div[4]/div/select'
        element = self.base.find_ele('xpath', xpath_value)
        Select(element).select_by_index(x)
        cert_xpath = '//*[@id="AddEditForm"]/div[2]/div[3]/div[2]/div[2]/div/div[1]/div[7]/div/input[1]'
        self.base.find_ele('xpath', cert_xpath).send_keys(cert_num)
    def write_ticketno(self):
        name_value = 'TicketNo_1'
        self.base.find_ele('name', name_value).send_keys('000-0000000001')
    # 填写订单价格信息
    def write_buyprice(self):
        name_value = 'BuyPrice'
        self.base.move_screen('name', name_value)
        self.base.find_ele('name', name_value).send_keys('600')
    def choose_Purchasingmessage(self, x, y):
        name_value1 = 'PurchasingChannel'
        element = self.base.find_ele('name', name_value1)
        Select(element).select_by_index(x)
        name_value2 = 'PurchasingPayType'
        element = self.base.find_ele('name', name_value2)
        Select(element).select_by_index(y)
    # 自主信息
    def choose_pat(self):
        name_value = 'PatMainReason'
        element = self.base.find_ele('name', name_value)
        Select(element).select_by_index(1)
    def inlandrecord_submit(self):
        name_value = 'submit'
        self.base.find_ele('name', name_value).click()

    def write_company_message(self):
        self.write_company()
        self.write_reservation()
        self.write_pnr()

    def write_flight_message(self):
        self.write_cityfrom()
        self.write_cityend()
        self.write_flightno()
        self.write_carbin()
        self.write_salecount()
        self.write_filghtdate()
        self.write_starttime()
        self.write_endtime()
        self.write_airrax()
        self.write_fuel()
        self.write_totalprice()
        self.write_facevalue()
        self.write_transferprice()
        self.write_buycount()

    def write_passanger_message(self):
        self.write_cname()
        self.choose_passagetype(1)
        self.choose_cert(2, 'huluwa')
        self.write_ticketno()

    def write_buy_message(self):
        self.write_buyprice()
        self.choose_Purchasingmessage(1,1)

    def submit_message(self):
        self.choose_pat()
        self.inlandrecord_submit()