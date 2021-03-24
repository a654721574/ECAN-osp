
import time
from selenium.webdriver.common.by import By
from common.base_page import BasePage
class UserPage(BasePage):
    #基础管理
    basic_management = (By.XPATH,"//*[contains(text(),'基础管理')]")
    #用户管理
    user_management = (By.XPATH, "//*[contains(text(),'用户管理')]")
    """新增用户"""

    #新增
    userNew = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-background-ghost']")
    # 系统名称
    systemName = (By.XPATH, "//ul[@class='ant-select-selection__rendered']")
    # 选择系统
    systemChoice = (By.XPATH, "//span[@title='开发平台']")
    #用户名称
    userName = (By.ID, "username")
    #机构框
    officeFrame = (By.XPATH, "//span[text()='请选择机构']")
    #机构搜索框
    officeSearchBox=(By.XPATH,"//span[@class='ant-select-dropdown-search']//input")
    #机构名称
    officeName = (By.XPATH, "//li[@class='filter-node']")
    #角色
    role=(By.XPATH, "//div[text()='请选择角色']")
    selectRole=(By.XPATH,"//li[text()='自动化测试角色(勿删)']")
    #状态
    state=(By.XPATH,"//span[text()='有效']/preceding-sibling::span[1]")
    state2=(By.XPATH,"//span[text()='有效']")

    #滚动
    a=(By.XPATH,"//label[@title='工资奖金密码'] ")
    #性别
    sex=(By.XPATH,"//span[text()='保密']/preceding-sibling::span[1]")
    sex2=(By.XPATH,"//span[text()='保密']")
    """查询用户"""
    #用户名
    name=(By.XPATH,"//span[@class='ant-form-item-children']//input[@class='ant-input']")
    #查询
    query=(By.XPATH, "//span[text()='查 询']")

    """修改用户"""
    #修改按钮
    updata = (By.XPATH, "//td[@class='ant-table-row-cell-break-word']//i[@title='修改用户']")
    #邮箱
    email=(By.ID,"email")
    #真实姓名
    trueName=(By.ID,"trueName")
    #手机号
    mobile=(By.ID,"mobile")

    """删除用户"""
    # 用户名称
    selectName = (By.XPATH, "//td[text()='ceshi5527']/preceding-sibling::td[1]//span[@class='ant-checkbox']")
    delName=(By.XPATH, "//td[text()='ceshi5527']")
    # 删除
    delete = (By.XPATH, "//span[text()='删 除']")
    # 确定
    dete = (By.XPATH, "//span[text()='确 定']/parent::button[@class='ant-btn ant-btn-primary']")

    #提交
    # submit=(By.XPATH,"//span[text()='提 交']")
    submit=(By.XPATH,"//span[.='提 交']/parent::button")
    new_success_info=(By.XPATH,"//span[text()='新增用户成功，初始密码为123456']")
    query_success_info = (By.XPATH, "//td[text()='ceshi5527']")
    updata_success_info = (By.XPATH, "//span[text()='修改用户成功']")
    del_success_info = (By.XPATH, "//span[text()='删除成功']")
    #公共操作
    def public(self):
        # 点击基础管理
        self.move_click(self.basic_management)
        self.scroll(self.user_management)
        # 点击用户管理
        self.move_click(self.user_management)
    #新增操作
    def newUser(self,name,username,officename):
        UserPage.public(self)
        #输入用户名
        self.input(self.name,name)
        time.sleep(1)
        #点击查询
        self.js_click(self.query)
        time.sleep(2)
        flag=self.isElementExist(self.query_success_info)
        if flag:
            # 选择用户名
            self.move_click(self.selectName)
            # 点击删除
            self.move_click(self.delete)
            # 点击确定
            self.move_click(self.dete)
            time.sleep(0.8)
            #点击新增
            self.move_click(self.userNew)
            # 点击系统名称框
            self.move_click(self.systemName)
            time.sleep(0.5)
            # 选择系统
            print("系统名称：", self.text(self.systemChoice))

            self.move_click(self.systemChoice)
            self.move_click(self.systemName)
            #输入用户名称
            self.input(self.userName,username)
            print("用户名：",username)
            #点击机构框
            self.move_click(self.officeFrame)
            #输入机构
            self.input(self.officeSearchBox, officename)
            print("机构：",officename)
            #选择机构
            self.move_click(self.officeName)
            #点击角色框
            self.move_click(self.role)
            time.sleep(0.5)
            self.scroll(self.selectRole)
            #选择角色
            self.move_click(self.selectRole)
            print("角色：",self.text(self.selectRole))
            #选择状态
            self.move_click(self.state)
            print("状态",self.text(self.state2))
            time.sleep(0.5)
            self.scroll(self.sex)
            #选择性别
            self.move_click(self.sex)
            print("性别：",self.text(self.sex2))
            time.sleep(0.5)
            # 点击提交
            self.move_click(self.submit)
            time.sleep(2)
        else:
            # 点击新增
            self.move_click(self.userNew)
            # 点击系统名称框
            self.move_click(self.systemName)
            time.sleep(0.5)
            # 选择系统
            print("系统名称：", self.text(self.systemChoice))

            self.move_click(self.systemChoice)
            self.move_click(self.systemName)
            # 输入用户名称
            self.input(self.userName, username)
            print("用户名：", username)
            # 点击机构框
            self.move_click(self.officeFrame)
            # 输入机构
            self.input(self.officeSearchBox, officename)
            print("机构：", officename)
            # 选择机构
            self.move_click(self.officeName)
            # 点击角色框
            self.move_click(self.role)
            time.sleep(0.5)
            self.scroll(self.selectRole)
            # 选择角色
            self.move_click(self.selectRole)
            print("角色：", self.text(self.selectRole))
            # 选择状态
            self.move_click(self.state)
            print("状态", self.text(self.state2))
            time.sleep(0.5)
            self.scroll(self.sex)
            # 选择性别
            self.move_click(self.sex)
            print("性别：", self.text(self.sex2))
            time.sleep(0.5)
            # 点击提交
            self.move_click(self.submit)
            time.sleep(2)


    #查询操作
    def queryUser(self,name):
        UserPage.public(self)
        time.sleep(1)
        #输入用户名
        self.input(self.name,name)
        time.sleep(1)
        #点击查询
        self.js_click(self.query)
        time.sleep(2)

    def updataUser(self,name,email,truename,mobile):
        UserPage.queryUser(self,name)
        #点击修改
        self.move_click(self.updata)
        #输入邮箱
        self.input(self.email,email)
        print("邮箱：",email)
        #输入真实姓名
        self.input(self.trueName,truename)
        print("真实姓名：",truename)
        #输入手机号
        self.input(self.mobile,mobile)
        print("手机号码：",mobile)
        #点击提交
        self.move_click(self.submit)
        time.sleep(2)

    def delUser(self,name):
        UserPage.queryUser(self,name)
        print("要删除的用户：",self.text(self.delName))
        #选择用户名
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
        success_elem=self.wait_presence_element(self.updata_success_info)
        return  success_elem.text
    #删除校验
    def get_del_success_msg(self):
        success_elem=self.wait_presence_element(self.del_success_info)
        return  success_elem.text


