"""
存储每个页面的通用行为。

"""
import logging
import os
import time
# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import Setting

class BasePage:
    url='/#/login'
    def __init__(self,driver:Chrome,load_timeout=10):
        self.driver = driver
        self.driver.set_page_load_timeout(load_timeout)

    def get(self):
        """
        封装get方法
        :return:
        """
        try:
            login_url = Setting.host + self.url
            return self.driver.get(login_url)
        except TimeoutException:
            self.driver.execute_script("window.stop()")

    def screenshot(self):
        """保存截图
        时间戳
        """
        # 文件名
        img_path = Setting.img_path
        filename = str(int(time.time())) + '.png'
        file = os.path.join(img_path, filename)
        self.driver.save_screenshot(file)
        return file


    def get_element(self, locator):
        """查找元素"""
        try:
            e = self.driver.find_element(*locator)
            return e
        except NoSuchElementException as e:
            logging.error("查找元素失败")
            self.screenshot()
            # 截图

    def wait_clickable_element(self, locator, timeout=30, poll=0.2):
        """等待元素可以被点击"""
        try:
            e = WebDriverWait(self.driver, timeout, poll).until(
                EC.element_to_be_clickable(locator)
            )
            return e
        except TimeoutException as e:
            logging.error("元素点击失败")
            self.screenshot()

    def wait_presence_element(self, locator, timeout=30, poll=0.2):
        """等待元素出现"""
        try:
            e = WebDriverWait(self.driver, timeout, poll).until(
                EC.presence_of_element_located(locator)
            )
            return e
        except TimeoutException as e:
            logging.error("元素未出现")
            self.screenshot()

    def wait_visible_element(self, locator, timeout=30, poll=0.2):
        """等待元素可见"""
        try:
            e = WebDriverWait(self.driver, timeout, poll).until(
                EC.visibility_of_element_located(locator)
            )
            return e
        except TimeoutException as e:
            logging.error("元素不可见")
            self.screenshot()

    def isElementExist(self, element):
        """
        判断元素是否存在
        :param element:
        :return:
        """
        flag = True
        try:
            # self.get_element(element)
            # WebDriverWait(self.driver,2).until(
            #     EC.presence_of_element_located(element)
            # )
            self.driver.find_element(*element)
            # self.driver.find_element(*element)
            return flag

        except:
            flag = False
            return flag
    def input(self, name_prop,  data):
        """全局文件输入，输入框
        e.send_keys()
        """
        # e=self.wait_presence_element(locator)
        e = self.get_element(name_prop)
        e.send_keys(data)

    def clear(self,name_prop):
        """
        清除
        :param name_prop:
        :return:
        """
        e=self.get_element(name_prop)
        webdriver.ActionChains(self.driver).move_to_element(e).double_click(e).perform()
        e.clear()
    def js_clear(self,locator):
        """
        js清除
        :return:
        """
        e=self.get_element(locator)
        js = 'document.querySelector("{}").value="";'.format(e)
        self.driver.execute_script(js)

    def click(self, locator):
        """click 点击"""
        e=self.wait_clickable_element(locator)
        e.click()
    def move_click(self, locator):
        """鼠标点击"""
        ele= self.wait_clickable_element(locator)
        webdriver.ActionChains(self.driver).move_to_element(ele).click(ele).perform()

    def double_click(self, locator):
        """鼠标双击"""
        ele = self.wait_clickable_element(locator)
        webdriver.ActionChains(self.driver).double_click(ele).perform()

    def js_click(self,locator):
        """js_click 点击"""
        try:
            ele= self.wait_clickable_element(locator)
            self.driver.execute_script("arguments[0].click();", ele)
        except Exception as e:
            assert  e
            logging.error("点击元素失败")
            self.screenshot()

        # 内嵌滚动条
    def scroll(self, locator):
        ele = self.get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    def text(self,locator):
        ele=self.wait_presence_element(locator)
        return ele.text











