"""

"""
import time

from selenium.webdriver.common.by import By
from config import Setting
from common.base_page import BasePage


class LoginPage(BasePage):
    """登录页面"""
    # url = '/#/ygt/login'

    user = (By.ID, 'name')
    pwd = (By.ID, 'password')
    btn = (By.XPATH, "//span[text()='登 录']/..")
    error_info_locator = (By.XPATH, "//div[text()='请输入账户名']")
    error_info_locator2 = (By.XPATH, "//div[text()='请输入密码']")
    invalid_info_locator = (By.XPATH, "//div[text()='用户名不存在']")
    success_info=(By.XPATH,"//h1[@class='animated fadeIn']")

    def login(self, username, pwd):
        """登录操作"""
        self.get()

        # 定位用户名
        user_elem = self.get_element(self.user)
        # 3， 输入用户名；
        user_elem.send_keys(username)

        # 4， 定位密码；
        pwd_elem = self.get_element(self.pwd)
        # 5, 输入密码
        pwd_elem.send_keys(pwd)

        # 6, 定位登录按钮；
        # btn_elem = self.get_element(self.btn)
        # 7,点击登录按钮；
        time.sleep(0.5)
        # btn_elem.click()
        self.move_click(self.btn)
        time.sleep(1.5)




    def get_error_msg(self):
        """获取错误信息"""
        error_elem = self.wait_presence_element(self.error_info_locator)
        return error_elem.text

    def get_error_msg2(self):
        """获取错误信息"""
        error_elem2 = self.wait_presence_element(self.error_info_locator2)
        return error_elem2.text

    def get_invalid_msg(self):
        """获取未授权信息"""
        invalid_elem = self.wait_presence_element(self.invalid_info_locator)
        return invalid_elem.text

    def get_success_msg(self):
        success_elem=self.wait_presence_element(self.success_info)
        return  success_elem.text



