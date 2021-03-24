import allure
import pytest

from data.login_data import login_data_error, login_data_error2, login_data_invalid, login_data_success

from pages.login_page import LoginPage



class TestLogin:

    @pytest.mark.parametrize('test_info', login_data_error)
<<<<<<< HEAD
    @pytest.mark.flaky(reruns=1)
=======
>>>>>>> gitee/master
    @allure.feature('登录模块')
    @allure.story("用户名密码为空")
    @allure.title("执行登录用户名密码为空测试用例")
    def test_login_username_empty(self, test_info, get_browser):
        print("-----执行登录用户名密码为空测试用例-----")

        driver = get_browser

        LoginPage(driver).login(test_info["user"], test_info["pwd"])
        print("------------测试数据---------")
        print("用户名：",test_info["user"])
        print("密码：",test_info["pwd"])

        expected = test_info['expected']
        error_msg = LoginPage(driver).get_error_msg()
        print("--------断言结果---------")

        print("实际结果",error_msg)
        print("预期结果",expected)

        try:
            assert error_msg == expected
        except AssertionError as e:
            raise e

    @pytest.mark.parametrize('test_info', login_data_error2)
<<<<<<< HEAD
    @pytest.mark.flaky(reruns=1)
=======
>>>>>>> gitee/master
    @allure.feature('登录模块')
    @allure.story("登录密码为空")
    @allure.title("执行登录密码为空测试用例")
    def test_login_username_empty2(self, test_info, get_browser):
        print("------执行登录密码为空测试用例------")
        driver = get_browser
        expected = test_info['expected']
        LoginPage(driver).login(test_info["user"], test_info["pwd"])
        print("------------测试数据---------")
        print("用户名：", test_info["user"])
        print("密码：", test_info["pwd"])
        error_msg = LoginPage(driver).get_error_msg2()
        print("--------断言结果---------")
        print("实际结果", error_msg)
        print("预期结果", expected)
        try:
            assert error_msg == expected
        except AssertionError as e:
            raise e

    @pytest.mark.parametrize('test_info', login_data_invalid)
<<<<<<< HEAD
    @pytest.mark.flaky(reruns=1)
=======
>>>>>>> gitee/master
    @allure.feature('登录模块')
    @allure.story("用户名不存在")
    @allure.title("执行登录用户名不存在测试用例")
    def test_login_invalid_user(self, test_info, get_browser):
        print("------执行登录用户名不存在测试用例------")
        driver = get_browser
        expected = test_info['expected']
        LoginPage(driver).login(test_info["user"], test_info["pwd"])
        print("------------测试数据---------")
        print("用户名：", test_info["user"])
        print("密码：", test_info["pwd"])
        invalid_msg = LoginPage(driver).get_invalid_msg()
        print("--------断言结果---------")
        print("实际结果", invalid_msg)
        print("预期结果", expected)
        try:
            assert invalid_msg==expected
        except AssertionError as e:
            raise e

    @pytest.mark.parametrize('test_info', login_data_success)
<<<<<<< HEAD
    @pytest.mark.flaky(reruns=1)
=======
>>>>>>> gitee/master
    @allure.feature('登录模块')
    @allure.story("登录成功")
    @allure.title("执行登录成功测试用例")
    def test_login_success_user(self, test_info, get_browser):
        print("------执行登录成功测试用例------")
        driver=get_browser
        expected = test_info['expected']
        LoginPage(driver).login(test_info["user"], test_info["pwd"])
        print("------------测试数据---------")
        print("用户名：", test_info["user"])
        print("密码：", test_info["pwd"])
        success_msg = LoginPage(driver).get_success_msg()
        print("--------断言结果---------")
        print("实际结果", success_msg)
        print("预期结果", expected)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e