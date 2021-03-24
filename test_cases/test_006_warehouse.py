import allure
import pytest
from config.user_config import User, User2
from data.warehouse_data import new_warehouse_data_success, query_warehouse_data_success, updata_warehouse_data_success, \
    del_warehouse_data_success
from pages.login_page import LoginPage

from pages.warehouse_page import WarehousePage



class TestWarehouse:


    """
    新增仓库成功
    """
    @pytest.mark.parametrize('test_info', new_warehouse_data_success)
    @pytest.mark.flaky(reruns=1)
    @allure.feature('仓库管理模块')
    @allure.story("新增仓库")
    @allure.title("执行新增仓库测试用例")
    @allure.description("新增仓库成功")
    def test_new_success(self, test_info, get_browser):
        driver = get_browser
        LoginPage(driver).login(User2.username, User2.pwd)
        expected = test_info['expected']
        WarehousePage(driver).newWarehouse(test_info["name"],test_info["warehousename"],test_info["warehousecode"])
        success_msg = WarehousePage(driver).get_new_success_msg()
        print(success_msg)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e
    """
    查询仓库成功
    """
    @pytest.mark.parametrize('test_info', query_warehouse_data_success)
    @allure.story("查询仓库名称")
    def test_query_success(self, test_info, get_browser):
        driver = get_browser
        LoginPage(driver).login(User2.username, User2.pwd)
        expected = test_info['expected']
        WarehousePage(driver).queryWarehouse(test_info["name"])
        success_msg = WarehousePage(driver).get_query_success_msg()
        print(success_msg)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e



    """
    修改仓库成功
    """
    @pytest.mark.parametrize('test_info', updata_warehouse_data_success)
    @allure.story("修改仓库成功")
    def test_updata_success(self, test_info, get_browser):
        driver = get_browser
        LoginPage(driver).login(User2.username, User2.pwd)
        expected = test_info['expected']
        WarehousePage(driver).updataWarehouse(test_info["name"])
        success_msg = WarehousePage(driver).get_updata_success_msg()
        print(success_msg)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e

    """
    删除仓库成功
    """
    @pytest.mark.parametrize('test_info', del_warehouse_data_success)
    @allure.story("删除仓库成功")
    def test_del_success(self, test_info, get_browser):
        driver = get_browser
        LoginPage(driver).login(User2.username, User2.pwd)
        expected = test_info['expected']
        WarehousePage(driver).delWarehouse(test_info["name"])
        success_msg = WarehousePage(driver).get_del_success_msg()
        print(success_msg)
        try:
            assert success_msg == expected
        except AssertionError as e:
            raise e