
import time
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from pages.login_page import LoginPage  #TODO 等会删掉
class OfficePage(BasePage):
    #基础管理
    basic_management = (By.XPATH,"//*[contains(text(),'基础管理')]")
    #组织机构设置
    office_setup = (By.XPATH, "//*[contains(text(),'组织机构设置')]")

    """新增"""
    #新增
    officeNew = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-background-ghost']")
    #系统名称
    systemName=(By.XPATH,"//ul[@class='ant-select-selection__rendered']")
    #选择系统
    systemChoice=(By.XPATH,"//span[@title='开发平台']")
    #机构名称
    officeName = (By.ID, "officeName")
    #是否启用
    whether_enable = (By.XPATH, "//div[@id='isStop']//div[@class='ant-select-selection__rendered']")
    #启用
    enable=(By.XPATH,"//li[text()='启用']")
    #组织机构代码
    officeCode=(By.ID,"officeCode")
    # 用于删除
    selectName1 = (By.XPATH, "//td[text()='测试5527']/preceding-sibling::td[1]//span[@class='ant-checkbox']")

    """查询"""
    #名称
    name=(By.XPATH,"(//label[text()='名称']/../following-sibling::div[1]//input)[1]")
    #查询
    query=(By.XPATH,"//span[text()='查 询']")

    """修改"""
    updata=(By.XPATH,"//td[@class='ant-table-row-cell-break-word']//i[@title='修改']")
    officeName2 = (By.ID, "officeName")

    """删除"""
    #机构名称
    selectName=(By.XPATH,"//td[text()='测试5528']/preceding-sibling::td[1]//span[@class='ant-checkbox']")
    delName=(By.XPATH,"//td[text()='测试5528']")
    #删除
    delete=(By.XPATH,"//span[text()='删 除']")
    #确定
    dete=(By.XPATH,"//span[text()='确 定']/parent::button[@class='ant-btn ant-btn-primary']")

    #提交
    # submit=(By.XPATH,"//span[text()='提 交']")
    submit=(By.XPATH,"//span[.='提 交']/parent::button")
    # submit="//span[.='提 交']/parent::button"
    new_success_info=(By.XPATH,"//span[text()='新增机构成功']")
    query_success_info=(By.XPATH,"//td[text()='测试5527']")
    updata_success_info=(By.XPATH,"//span[text()='修改机构成功']")
    del_success_info=(By.XPATH,"//span[text()='删除成功']")
    def public(self):
        # 点击基础管理
        self.move_click(self.basic_management)
        # 点击组织机构设置
        self.move_click(self.office_setup)
        # # 点击新增
        # self.move_click(self.officeNew)
    #新增操作
    def newOffice(self,name,officename,officecode):
        OfficePage.public(self)

        # 输入名称
        self.input(self.name, name)
        # 点击查询
        self.move_click(self.query)
        time.sleep(1.5)
        #判断机构是否存在
        flag=self.isElementExist(self.query_success_info)
        if flag:
            self.move_click(self.selectName1)
            # 点击删除
            self.move_click(self.delete)
            # 点击确定
            self.move_click(self.dete)
            time.sleep(0.5)
            #点击新增
            self.move_click(self.officeNew)
            # 点击系统名称框
            self.move_click(self.systemName)
            time.sleep(0.5)
            # 选择系统
            print("系统名称：",self.text(self.systemChoice))

            self.move_click(self.systemChoice)
            self.move_click(self.systemName)
            #输入机构名称
            self.input(self.officeName,officename)
            print("机构名称：",officename)
            #点击是否启用
            self.move_click(self.whether_enable)
            time.sleep(0.5)
            #选择启用
            print("是否启用：",self.text(self.enable))
            self.move_click(self.enable)
            #组织机构代码
            self.input(self.officeCode,officecode)
            print("组织机构代码:",officecode)
            # time.sleep(0.5)
            # 点击提交
            self.move_click(self.submit)
            time.sleep(0.5)
            self.move_click(self.submit)
            time.sleep(2)
        else:
            # 点击新增
            self.move_click(self.officeNew)
            # 点击系统名称框
            self.move_click(self.systemName)
            # 选择系统
            time.sleep(0.5)
            print("系统名称：",self.text(self.systemChoice))
            self.move_click(self.systemChoice)
            self.move_click(self.systemName)
            # 输入机构名称
            self.input(self.officeName, officename)
            print("机构名称：", officename)
            # 点击是否启用
            self.move_click(self.whether_enable)
            time.sleep(0.5)

            print("是否启用：", self.text(self.enable))
            # 选择启用
            self.move_click(self.enable)
            # 组织机构代码
            self.input(self.officeCode, officecode)
            print("组织机构代码:", officecode)
            # time.sleep(0.5)
            # 点击提交
            self.move_click(self.submit)
            time.sleep(0.5)
            self.move_click(self.submit)

            time.sleep(2)

    #查询操作
    def queryOffice(self,name):
        OfficePage.public(self)
        #输入名称
        self.input(self.name,name)
        # print("要查询的机构：",name)
        #点击查询
        self.move_click(self.query)
        time.sleep(2)

    #修改操作
    def updataOffice(self,name,officename):
        OfficePage.queryOffice(self,name)
        #点击修改
        self.move_click(self.updata)

        #清除机构名称
        self.move_click(self.officeName2)
        time.sleep(1)
        js = 'document.querySelector("#officeName").value="";'
        self.driver.execute_script(js)
        time.sleep(0.5)
        #输入机构名称
        self.input(self.officeName2,officename)
        print("修改机构名称：",officename)
        # 点击提交
        self.move_click(self.submit)
        time.sleep(2)

    #删除操作
    def delOffice(self,name):
        OfficePage.queryOffice(self, name)
        #选择要删除的机构
        print("删除的机构：",self.text(self.delName))
        self.move_click(self.selectName)
        #点击删除
        self.move_click(self.delete)
        #点击确定
        self.move_click(self.dete)
        time.sleep(2)

    #新增校验
    def get_new_success_msg(self):
        success_elem=self.wait_presence_element(self.new_success_info)
        return  success_elem.text

    #查询校验
    def get_query_success_msg(self):
       success_elem=self.wait_presence_element(self.query_success_info)
       return  success_elem.text

    #修改校验
    def get_updata_success_msg(self):
        success_elem = self.wait_presence_element(self.updata_success_info)
        return success_elem.text

    # 删除校验
    def get_del_success_msg(self):
        success_elem = self.wait_presence_element(self.del_success_info)
        return success_elem.text


