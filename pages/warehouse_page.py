
import time
from selenium.webdriver.common.by import By
from common.base_page import BasePage
class WarehousePage(BasePage):
    #基础管理
    basic_management = (By.XPATH,"//*[contains(text(),'基础管理')]")
    #仓库管理
    warehouse_management = (By.XPATH, "//*[contains(text(),'仓库管理')]")
    """新增仓库"""
    #新增
    warehouseNew = (By.XPATH, "//span[contains(text(),'新增仓库')]/..")
    #仓库名称
    warehouseName = (By.ID, "hrp_warehouse#name@search新增仓库名称")
    #仓库编号
    warehouseCode = (By.ID, "hrp_warehouse#code@search新增仓库编号")
    #所属系统
    system=(By.XPATH,"//div[@class='ant-modal-content']//div[@class='ant-select-selection ant-select-selection--multiple']//div[@class='ant-select-selection__rendered']")
    selectSystem=(By.XPATH,"//li[contains(text(),'人事')]")
    #建帐年份
    year = (By.XPATH, "(//input[@class='ant-calendar-picker-input ant-input'])[1]")
    selectYear=(By.XPATH,"//td[@title='2020']/a")
    #建帐月份
    month=(By.XPATH, "(//input[@class='ant-calendar-picker-input ant-input'])[2]")
    selectMonth=(By.XPATH,"//td[@title='九月']/a")

    """查询仓库"""
    name=(By.XPATH,"(//label[text()='仓库名称']/../following-sibling::div[1]//input)[1]")
    # 查询
    query = (By.XPATH, "//span[text()='查询数据']")
    """修改仓库"""

    updata=(By.XPATH,"//span[text()='修 改']")
    # 所属系统
    system2 = (By.XPATH,
              "//div[@class='ant-modal-content']//div[@class='ant-select-selection ant-select-selection--multiple']//div[@class='ant-select-selection__rendered']")
    selectSystem2 = (By.XPATH, "//li[contains(text(),'财务')]")

    """删除仓库"""
    selectName = (By.XPATH, "//div[text()='测试仓库5527']/../preceding-sibling::td[3]//span[@class='vxe-cell--checkbox']")
    delName=(By.XPATH,"//div[text()='测试仓库5527']")
<<<<<<< HEAD
    delete=(By.XPATH,"//span[contains(text(),'删除仓库')]")
=======
    delete=(By.XPATH,"//span[text()='删 除']")
>>>>>>> gitee/master
    # 确定
    dete = (By.XPATH, "//span[text()='确 定']")

    #提交
    submit=(By.XPATH,"//span[contains(text(),'保存修改')]")
    # submit="//span[.='提 交']/parent::button"
    new_success_info=(By.XPATH,"//span[text()='新增成功']")
    query_success_info = (By.XPATH, "//div[text()='测试仓库5527']")
    updata_success_info = (By.XPATH, "//span[text()='修改成功']")
    del_success_info = (By.XPATH, "//span[text()='删除成功']")

    #公共操作
    def public(self):
        # 点击基础管理
        self.move_click(self.basic_management)
        # 点击仓库管理
        self.move_click(self.warehouse_management)

    #新增仓库操作
    def newWarehouse(self,name,warehousename,warehousecode):
        WarehousePage.public(self)
        #输入仓库名称
        self.input(self.name,name)
        #点击查询
        self.move_click(self.query)
        time.sleep(2)
        flag=self.isElementExist(self.query_success_info)
        if flag:
            # 选择仓库名称
            self.move_click(self.selectName)
            # 点击删除
            self.move_click(self.delete)

            # 点击确定
            self.move_click(self.dete)
            time.sleep(1)
            #点击新增
            self.move_click(self.warehouseNew)

            #输入仓库名称
            self.input(self.warehouseName,warehousename)
            print("仓库名称：",warehousename)
            #输入仓库编码
            self.input(self.warehouseCode,warehousecode)
            print("仓库编码:",warehousecode)
            #点击所属系统框
            self.move_click(self.system)
            #选择系统
            print(self.text(self.selectSystem))
            self.move_click(self.selectSystem)
            self.move_click(self.system)
            #点击建帐年份
            self.move_click(self.year)
            #选择年份
            self.move_click(self.selectYear)
            #点击建帐月份
            self.move_click(self.month)
            #选择月份
            self.move_click(self.selectMonth)
            time.sleep(1)
            # 点击提交
            self.move_click(self.submit)
            time.sleep(1.5)
        else:
            # 点击新增
            self.move_click(self.warehouseNew)
            # 输入仓库名称
            self.input(self.warehouseName, warehousename)
            print("仓库名称：", warehousename)
            # 输入仓库编码
            self.input(self.warehouseCode, warehousecode)
            print("仓库编码:", warehousecode)
            # 点击所属系统框
            self.move_click(self.system)
            # 选择系统
            self.move_click(self.selectSystem)
            self.move_click(self.system)
            # 点击建帐年份
            self.move_click(self.year)
            # 选择年份
            self.move_click(self.selectYear)
            # 点击建帐月份
            self.move_click(self.month)
            # 选择月份
            self.move_click(self.selectMonth)
            time.sleep(1)
            # 点击提交
            self.move_click(self.submit)
            time.sleep(1.5)

    #查询仓库操作
    def queryWarehouse(self,name):
        WarehousePage.public(self)
        #输入仓库名称
        self.input(self.name,name)
        #点击查询
        self.move_click(self.query)
        time.sleep(2)

    #修改仓库操作
    def updataWarehouse(self,name):
        WarehousePage.queryWarehouse(self,name)
        #点击修改
        self.move_click(self.updata)
        #点击系统框
        self.move_click(self.system2)
        time.sleep(1)
        #选择系统
        print("选择要修改的系统：",self.text(self.selectSystem2))
        self.move_click(self.selectSystem2)
        time.sleep(0.5)
        self.move_click(self.system2)
        self.move_click(self.submit)
        time.sleep(1.5)

    #删除仓库操作
    def delWarehouse(self,name):
        WarehousePage.queryWarehouse(self,name)
        #选择仓库名称
        self.move_click(self.selectName)
        #点击删除
        self.move_click(self.delete)
        #点击确定
        self.move_click(self.dete)
        time.sleep(1.5)
    #新增仓库检验
    def get_new_success_msg(self):
        success_elem=self.wait_presence_element(self.new_success_info)
        return  success_elem.text

    #查询仓库检验
    def get_query_success_msg(self):
        success_elem=self.wait_presence_element(self.query_success_info)
        return  success_elem.text

    #修改仓库检验
    def get_updata_success_msg(self):
        success_elem=self.wait_presence_element(self.updata_success_info)
        return  success_elem.text

    #删除仓库检验
    def get_del_success_msg(self):
        success_elem=self.wait_presence_element(self.del_success_info)
        return  success_elem.text


