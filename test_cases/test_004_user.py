import allure
import pytest
from config.user_config import User
from data.user_data import new_user_data_success, query_user_data_success, updata_user_data_success, \
    del_user_data_success
from pages.login_page import LoginPage
from pages.user_page import UserPage


class TestUser:
    """
    新增用户成功
    """
    @pytest.mark.parametrize('test_info',new_user_data_success)
    @pytest.mark.flaky(reruns=1)
    @allure.feature('用户管理模块')
    @allure.story("新增用户")
    @allure.title("执行新增用户测试用例")
    @allure.description("新增用户成功")
    def test_new_success(self,test_info,get_browser):
        driver=get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行新增用户测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        UserPage(driver).newUser(test_info["name"],test_info["username"],test_info["officename"])
        success_msg = UserPage(driver).get_new_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg ==expected
        except AssertionError as e:
            raise e

    """
    查询用户成功
    """
    @pytest.mark.parametrize('test_info',query_user_data_success)
    @pytest.mark.flaky(reruns=1)
    @allure.feature('用户管理模块')
    @allure.story("查询用户")
    @allure.title("执行查询用户测试用例")
    @allure.description("查询用户成功")
    def test_query_success(self,test_info,get_browser):
        driver=get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行查询用户测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        UserPage(driver).queryUser(test_info["name"])
        print("要查询的用户：", test_info["name"])
        success_msg = UserPage(driver).get_query_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg ==expected
        except AssertionError as e:
            raise e

    """
      修改用户成功
      """

    @pytest.mark.parametrize('test_info', updata_user_data_success)
    @allure.feature('用户管理模块')
    @allure.story("修改用户")
    @allure.title("执行修改用户测试用例")
    @allure.description("修改用户成功")
    def test_updata_success(self, test_info, get_browser):
        driver = get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行修改用户测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        UserPage(driver).updataUser(test_info["name"],test_info["email"],test_info["truename"],test_info["mobile"])
        success_msg = UserPage(driver).get_updata_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e

    """
      删除用户成功
      """

    @pytest.mark.parametrize('test_info', del_user_data_success)
    @allure.feature('用户管理模块')
    @allure.story("删除用户")
    @allure.title("执行删除用户测试用例")
    @allure.description("删除用户成功")
    def test_del_success(self, test_info, get_browser):
        driver = get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行删除用户测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        UserPage(driver).delUser(test_info["name"])
        success_msg = UserPage(driver).get_del_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e

