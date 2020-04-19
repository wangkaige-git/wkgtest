#coding=utf-8
from base.common_method import CommonMethod
from page.home_page import HomePage
from page.reserve_page import ReservePage
from selenium import webdriver
from handle.inlandrecord_handle import InlandRecordHandle
from handle.home_handle import HomeHandle

driver = webdriver.Chrome()
base = CommonMethod(driver)
homepage = HomePage(driver)
homehandle = HomeHandle(driver)
reservepage = ReservePage(driver)
inrecord = InlandRecordHandle(driver)

base.login_in()
base.close_hint()
homehandle.airport()
homehandle.record_order()





