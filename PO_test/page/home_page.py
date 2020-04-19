# coding=utf-8
from base.base_method import BaseMethod
from selenium.webdriver.common.by import By
import time


class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.base = BaseMethod(self.driver)

    #关闭刚登陆进来的琅琊榜排行
    def close_hint(self):
        ele_xpath = '/html/body/div[3]/div/div[3]/div[3]/div[2]/div[1]/span'
        locator = (By.XPATH, ele_xpath)
        self.base.wait_element_located(locator)
        try:
            self.base.find_ele('xpath', ele_xpath).click()
        except:
            return None

    # 点击主页面的机票
    def airport(self):
        ele_xpath = '//*[@id="sidebar"]/ul/li[4]/a'
        return self.base.find_ele('xpath', ele_xpath).click()

    # 点击白屏下单
    def air_order(self):
        ele_xpath = '//*[@id="sidebar"]/ul/li[4]/ul/li[1]/a/span'
        locator = (By.XPATH, ele_xpath)
        self.base.wait_element_located(locator)
        return self.base.find_ele('xpath', ele_xpath).click()

    # 点击国内机票录单
    def record_order(self):
        ele_xpath = '//*[@id="sidebar"]/ul/li[4]/ul/li[4]/a/span'
        locator = (By.XPATH, ele_xpath)
        self.base.wait_element_located(locator)
        self.base.find_ele('xpath', ele_xpath).click()
        self.base.wait_title('国内机票订单录入')

    # 输入公司名
    def send_company(self, companyname):
        title = '白屏下单-机票查询'
        self.base.wait_title(title)
        value1 = '//*[@id="FlightQueryForm"]/div[1]/div/input[1]'
        value2 = '//*[@id="FlightQueryForm"]/div[1]/div/ul/li[1]'
        return self.base.send_and_choose('xpath', value1, 'xpath', value2, companyname)

    # 输入起始地点
    def send_orgcity(self, start_city):
        value1 = 'OrgCity'
        value2 = '/html/body/div[11]/ul/li'
        return self.base.send_and_choose('id', value1, 'xpath', value2, start_city)

    # 输入到达地点
    def send_dstcity(self, end_city):
        value1 = 'DstCity'
        value2 = '/html/body/div[12]/ul/li'
        return self.base.send_and_choose('id', value1, 'xpath', value2, end_city)

    # 选择航班时间
    def choose_time(self, flightdate):
        time_id = 'DepDate'
        self.base.find_ele('id', time_id).clear()
        self.base.find_ele('id', time_id).click()
        return self.base.find_ele('id', time_id).send_keys(flightdate)

    # 点击搜索
    def click_search(self):
        search_id = 'btnQuery'
        self.base.find_ele('id', search_id).click()
        time.sleep(10)

    # 获取航班列表
    def get_flightlist(self):
        flight_list = self.base.find_eles('class', 'FlightList')
        return len(flight_list)

    # 点击更多舱位（这里写死是点击加载出来的第一个航班）
    def more_carbin(self):
        ele_xpaths = "//*[text()='更多舱位信息']"
        elements = self.base.find_eles('xpath',ele_xpaths)
        element = elements[0]
        element.location_once_scrolled_into_view
        element.click()
        time.sleep(1)

    # 选择某个航班的协议价预定
    def choose_carbin(self, type='xieyijia'):
        xpath_value = '//*[@id="flightresult"]/ul[1]//*[@class="xieyijia"]/../..//*[@class="btn btn-darkorange btn-sm btnBooking"]'
        list = self.base.find_eles('xpath', xpath_value)
        self.driver.execute_script("arguments[0].scrollIntoView();", list[10])
        list[10].click()
        time.sleep(1)
        # if self.base.find_ele('xpath','/html/body/div[14]/div/div/div[1]'):
        #     raise Exception("企业为现付或状态不正常!")

    def backstate_search(self, companyname, start_city, end_city, flightdate='2020-03-08'):
        self.close_hint()
        self.airport()
        self.air_order()
        self.send_company(companyname)
        self.send_orgcity(start_city)
        self.send_dstcity(end_city)
        self.choose_time(flightdate)
        self.click_search()


