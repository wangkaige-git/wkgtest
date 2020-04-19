from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from base.read_config import ReadConfig
from selenium.webdriver.common.by import By
import time

class BaseMethod():

    def __init__(self,driver):
        self.config = ReadConfig('LocalElement.ini')
        self.driver = driver

    def start_chrome(self):
        url = self.config.get_config_value('RegisterElement','url')
        self.driver.get(url)
        self.driver.maximize_window()
        return self.driver

    #重新封装find_element函数
    def find_ele(self,key,value):
        try:
            if key == 'id':
                return self.driver.find_element_by_id(value)
            if key == 'xpath':
                return self.driver.find_element_by_xpath(value)
            if key == 'class':
                return self.driver.find_element_by_class_name(value)
            if key == 'name':
                return self.driver.find_element_by_name(value)
        except:
            return None
            #self.driver.save_screenshot('E:\\auto_test\\PO_test\\image\\%s.png' %value)

    #重新封装find_elements函数
    def find_eles(self,key,value):
        try:
            if key == 'id':
                return self.driver.find_elements_by_id(value)
            if key == 'xpath':
                return self.driver.find_elements_by_xpath(value)
            if key == 'class':
                return self.driver.find_elements_by_class_name(value)
            if key == 'name':
                return self.driver.find_elements_by_name(value)
        except:
            return None

    #等待元素出现
    def wait_element_located(self,locator):
        wait_method = expected_conditions.presence_of_element_located(locator)
        return WebDriverWait(self.driver,30,0.5).until(wait_method)

    #等待页面title出现
    def wait_title(self,title):
        method = expected_conditions.title_is(title)
        return WebDriverWait(self.driver,30,0.5).until(method)

    #不在当前屏幕范围的元素移动到当前屏幕
    def move_screen(self,by,value):
        if by == 'xpath':
            element = self.driver.find_element_by_xpath(value)
        if by == 'name':
            element = self.driver.find_element_by_name(value)
        element.location_once_scrolled_into_view


    #将鼠标滚轮移动到当前聚焦的元素处
    def focus_element(self,by,element):
        if by == 'id':
            new_driver = self.driver.find_element_by_id(element)
        elif by == 'xpath':
            new_driver = self.driver.find_element_by_xpath(element)
        elif by == 'class':
            new_driver = self.driver.find_element_by_class_name(element)
        self.driver.execute_script("arguments[0].scrollIntoView();",new_driver)

    #清除输入框内容，输入新内容并在下拉中选择结果
    def send_and_choose(self,by1,value1,by2,value2,send_key):
        self.find_ele(by1,value1 ).clear()
        self.find_ele(by1, value1).send_keys(send_key)
        if by2 == 'id':
            by_key = By.ID
        else:
            by_key = By.XPATH
        locator = (by_key,value2)
        if self.wait_element_located(locator):
            self.find_ele(by2,value2).click()

    #获取输入框内的值
    def get_value(self,key,value):
        return self.find_ele(key,value).get_attribute('value')

    #获取元素的文本
    def get_eletext(self,key,value):
        return self.find_ele(key,value).get_attribute('textContent')


if __name__ == '__main__':
    pass


