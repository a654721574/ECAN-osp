import allure
import pytest

from common.base_page import BasePage
from config.user_config import User

from data.office_data import new_office_data_success, query_office_data_success, updata_office_data_success, \
    del_office_data_success

from pages.login_page import LoginPage
from pages.office_page import OfficePage



class TestOffice:

    @pytest.mark.parametrize('test_info',new_office_data_success)
    @pytest.mark.flaky(reruns=1)
    @allure.feature('机构管理模块')
    @allure.story("新增机构")
    @allure.title("执行新增机构测试用例")
    @allure.description("新增机构成功")
    def test_new_success(self,test_info,get_browser):
        """
        新增机构成功
        :param test_info:
        :param get_browser:
        :return:
        """
        driver=get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行新增机构成功测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        OfficePage(driver).newOffice(test_info["name"],test_info["officename"], test_info["officecode"])
        success_msg = OfficePage(driver).get_new_success_msg()
        print("---------断言结果------------")
        print("实际结果：",success_msg)
        print("预期结果：", expected)

        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e

    @pytest.mark.parametrize('test_info', query_office_data_success)
    @pytest.mark.flaky(reruns=1)
    @allure.feature('机构管理模块')
    @allure.story("查询机构")
    @allure.title("执行查询机构测试用例")
    @allure.description("查询机构成功")
    def test_query_success(self, test_info, get_browser):
        """
        查询机构成功
        :param test_info:
        :param get_browser:
        :return:
        """
        driver = get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行查询机构成功测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        OfficePage(driver).queryOffice(test_info["name"])
        print("要查询的机构：",test_info["name"])
        success_msg = OfficePage(driver).get_query_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e

    @pytest.mark.parametrize('test_info', updata_office_data_success)
<<<<<<< HEAD
    @pytest.mark.flaky(reruns=1)
=======
>>>>>>> gitee/master
    @allure.feature('机构管理模块')
    @allure.story("修改机构")
    @allure.title("执行修改机构测试用例")
    @allure.description("修改机构成功")
    def test_updata_success(self, test_info, get_browser):
        """
        修改机构成功
        :param test_info:
        :param get_browser:
        :return:
        """
        driver = get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行修改机构成功测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        OfficePage(driver).updataOffice(test_info["name"],test_info["officename"])
        success_msg = OfficePage(driver).get_updata_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e

    @pytest.mark.parametrize('test_info', del_office_data_success)
    @allure.feature('机构管理模块')
    @allure.story("删除机构")
    @allure.title("执行删除机构测试用例")
    @allure.description("删除机构成功")
    def test_del_success(self, test_info, get_browser):
        """
        删除机构成功
        :param test_info:
        :param get_browser:
        :return:
        """
        driver = get_browser
        LoginPage(driver).login(User.username, User.pwd)
        print("-------执行删除机构成功测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        OfficePage(driver).delOffice(test_info["name"])

        success_msg = OfficePage(driver).get_del_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e