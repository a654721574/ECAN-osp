import allure
import pytest
from config.user_config import  User2
from data.dept_data import new_dept_data_success, query_dept_data_success, updata_dept_data_success, \
    del_dept_data_success
from pages.dept_page import DeptPage
from pages.login_page import LoginPage



class TestDept:

    """
    新增科室成功
    """
    @pytest.mark.parametrize('test_info', new_dept_data_success)
    @pytest.mark.flaky(reruns=1)
    @allure.feature('科室管理模块')
    @allure.story("新增科室")
    @allure.title("执行新增科室测试用例")
    @allure.description("新增科室成功")
    def test_new_success(self, test_info, get_browser):
        driver = get_browser
        LoginPage(driver).login(User2.username, User2.pwd)
        print("-------执行新增科室测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
<<<<<<< HEAD
        DeptPage(driver).newDept(test_info["name"],test_info["deptcode"],test_info["deptname"],test_info["deptlevel"])
=======
        DeptPage(driver).newDept(test_info["name"],test_info["deptcode"],test_info["deptname"])
>>>>>>> gitee/master
        success_msg = DeptPage(driver).get_new_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e


    """
    查询科室成功
    """
    @pytest.mark.parametrize('test_info', query_dept_data_success)
    @pytest.mark.flaky(reruns=1)
    @allure.feature('科室管理模块')
    @allure.story("查询科室")
    @allure.title("执行查询科室测试用例")
    @allure.description("查询科室成功")
    def test_query_success(self, test_info, get_browser):
        driver = get_browser
        LoginPage(driver).login(User2.username, User2.pwd)
        print("-------执行查询科室测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        DeptPage(driver).queryDept(test_info["name"])
        print("要查询的科室：", test_info["name"])
        success_msg = DeptPage(driver).get_query_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e

    """
    修改科室成功
    """
    @pytest.mark.parametrize('test_info', updata_dept_data_success)
    @allure.feature('科室管理模块')
    @allure.story("修改科室")
    @allure.title("执行修改科室测试用例")
    @allure.description("修改科室成功")
    def test_updata_success(self, test_info, get_browser):
        driver = get_browser
        LoginPage(driver).login(User2.username, User2.pwd)
        print("-------执行修改科室测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        DeptPage(driver).updataDept(test_info["name"],test_info["deptname"])
        success_msg = DeptPage(driver).get_updata_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e

    """
    删除科室成功
    """
    @pytest.mark.parametrize('test_info', del_dept_data_success)
    @allure.feature('科室管理模块')
    @allure.story("删除科室")
    @allure.title("执行删除科室测试用例")
    @allure.description("删除科室成功")
    def test_del_success(self, test_info, get_browser):
        driver = get_browser
        LoginPage(driver).login(User2.username, User2.pwd)
        print("-------执行删除科室测试用例----------")
        expected = test_info['expected']
        print("---------测试数据------------------")
        DeptPage(driver).delDept(test_info["name"])
        success_msg = DeptPage(driver).get_del_success_msg()
        print("---------断言结果------------")
        print("实际结果：", success_msg)
        print("预期结果：", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e