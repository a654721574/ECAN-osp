import allure
import pytest

from config.user_config import User
from data.menu_data import new_menu_data_success, query_menu_data_success, updata_menu_data_success, \
    del_menu_data_success

from pages.login_page import LoginPage
from pages.menu_page import MenuPage




class TestMenu:

    @pytest.mark.parametrize('test_info',new_menu_data_success)
    @pytest.mark.flaky(reruns=1)
    @allure.feature('菜单管理模块')
    @allure.story("新增菜单")
    @allure.title("执行新增菜单测试用例")
    @allure.description("新增菜单成功")
    def test_new_success(self,test_info,get_browser):
        """
        新增菜单成功
        :param test_info:
        :param get_browser:
        :return:
        """
        driver=get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行新增菜单测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        MenuPage(driver).newMenu(test_info["name"],test_info["menuname"], test_info["path"],test_info["component"])
        success_msg = MenuPage(driver).get_new_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e

    @pytest.mark.parametrize('test_info', query_menu_data_success)
    @pytest.mark.flaky(reruns=1)
    @allure.feature('菜单管理模块')
    @allure.story("查询菜单")
    @allure.title("执行查询菜单测试用例")
    @allure.description("查询菜单成功")
    def test_query_success(self, test_info, get_browser):
        """
        查询菜单成功
        :param test_info:
        :param get_browser:
        :return:
        """
        driver = get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行查询菜单测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        MenuPage(driver).queryMenu(test_info["name"])
        print("要查询的菜单：", test_info["name"])
        success_msg = MenuPage(driver).get_query_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e

    @pytest.mark.parametrize('test_info', updata_menu_data_success)
    @allure.feature('菜单管理模块')
    @allure.story("修改菜单")
    @allure.title("执行修改菜单测试用例")
    @allure.description("修改菜单成功")
    def test_updata_success(self, test_info, get_browser):
        """
        修改菜单成功
        :param test_info:
        :param get_browser:
        :return:
        """
        driver = get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行修改菜单测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        MenuPage(driver).updataMenu(test_info["name"],test_info["perms"],test_info["orderum"])
        success_msg = MenuPage(driver).get_updata_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e


    @pytest.mark.parametrize('test_info',del_menu_data_success)
    @allure.feature('菜单管理模块')
    @allure.story("删除菜单")
    @allure.title("执行删除菜单测试用例")
    @allure.description("删除菜单成功")
    def test_del_success(self, test_info, get_browser):
        """
        删除菜单成功
        :param test_info:
        :param get_browser:
        :return:
        """
        driver = get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行删除菜单测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        MenuPage(driver).delMenu(test_info["name"])
        success_msg = MenuPage(driver).get_del_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e