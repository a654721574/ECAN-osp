import allure
import pytest
from config.user_config import User
from data.role_data import new_role_data_success, query_role_data_success, updata_role_data_success, \
    del_role_data_success
from pages.login_page import LoginPage
from pages.role_page import RolePage

class TestRole:

    @pytest.mark.parametrize('test_info', new_role_data_success)
    @pytest.mark.flaky(reruns=1)
    @allure.feature('角色管理模块')
    @allure.story("新增角色")
    @allure.title("执行新增角色测试用例")
    @allure.description("新增角色成功")
    def test_new_success(self, test_info, get_browser):
        """
        新增角色成功
        :param test_info:
        :param get_browser:
        :return:
        """
        driver = get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行新增角色成功测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        RolePage(driver).newRole(test_info["name"],test_info["officename"], test_info["rolename"])
        success_msg = RolePage(driver).get_new_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e

    @pytest.mark.parametrize('test_info', query_role_data_success)
    @pytest.mark.flaky(reruns=1)
    @allure.feature('角色管理模块')
    @allure.story("查询角色")
    @allure.title("执行查询角色测试用例")
    @allure.description("查询角色成功")
    def test_query_success(self, test_info, get_browser):
        """
        查询角色成功
        :param test_info:
        :param get_browser:
        :return:
        """
        driver = get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行查询角色成功测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        RolePage(driver).queryRole(test_info["name"])
        print("要查询的角色：",test_info["name"])
        success_msg = RolePage(driver).get_query_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e

    @pytest.mark.parametrize('test_info', updata_role_data_success)
<<<<<<< HEAD
    @pytest.mark.flaky(reruns=1)
=======
>>>>>>> gitee/master
    @allure.feature('角色管理模块')
    @allure.story("修改角色")
    @allure.title("执行修改角色测试用例")
    @allure.description("修改角色成功")
    def test_updata_success(self, test_info, get_browser):
        """
        修改角色成功
        :param test_info:
        :param get_browser:
        :return:
        """
        driver = get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行修改角色成功测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        RolePage(driver).updata_Role(test_info["name"],test_info["roleescribe"])
        success_msg = RolePage(driver).get_updata_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e

    @pytest.mark.parametrize('test_info', del_role_data_success)
    @allure.feature('角色管理模块')
    @allure.story("删除角色")
    @allure.title("执行删除角色测试用例")
    @allure.description("删除角色成功")
    def test_del_success(self, test_info, get_browser):
        """
        删除角色成功
        :param test_info:
        :param get_browser:
        :return:
        """
        driver = get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行删除角色成功测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        RolePage(driver).del_Role(test_info["name"])

        success_msg = RolePage(driver).get_del_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e