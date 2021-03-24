
import time
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from pages.login_page import LoginPage  #TODO 等会删掉
class DeptPage(BasePage):
    #基础管理
    basic_management = (By.XPATH,"//*[contains(text(),'基础管理')]")
    #科室设置
    dept_management = (By.XPATH, "//*[contains(text(),'科室设置')]")
    """新增科室"""
    #新增
    deptNew = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-background-ghost']")
    #所需机构
    officeName=(By.XPATH,"//span[@id='officeId']")
    #选择机构
    officeselect=(By.XPATH,"//span[@title='自动化测试(勿删)']")
    #使用年限框
    yearsBox = (By.XPATH, "//div[@id='theYearType']//div[@class='ant-select-selection__rendered']")
    #年限
    years = (By.XPATH, "//li[text()='通用类型']")
    #是否启用
    isEnable=(By.XPATH,"//div[@id='isStop']//div[@class='ant-select-selection__rendered']")
    #启用
    Enable = (By.XPATH, "//li[text()='启用']")
    #科室编号
    deptCode=(By.ID, "id")
    #科室名称
    deptName=(By.ID,"deptName")
    #科室级别
    deptLevel=(By.XPATH,"//input[@placeholder='请输入科室级别']")
    #用于删除名称
    selectName1 = (By.XPATH, "//td[text()='测试科室5527']/preceding-sibling::td[2]//span[@class='ant-checkbox']")

    """查询科室"""
    #科室名称
    name=(By.XPATH,"(//label[text()='科室名称']/../following-sibling::div[1]//input)[1]")
    #查询
    query=(By.XPATH, "//span[text()='查 询']")

    """修改科室"""
    #修改按钮
    updata=(By.XPATH,"//td[@class='ant-table-row-cell-break-word']//i[@title='修改']")
    #科室名称
    deptName2 = (By.ID, "deptName")

    """删除科室"""
    #科室名称
    selectName=(By.XPATH,"//td[text()='测试科室5528']/preceding-sibling::td[2]//span[@class='ant-checkbox']")
    delName=(By.XPATH,"//td[text()='测试科室5528']")
    #删除
    delete=(By.XPATH,"//span[text()='删 除']")
    #确定
    dete=(By.XPATH,"//span[text()='确 定']/parent::button[@class='ant-btn ant-btn-primary']")

    #提交
    submit=(By.XPATH,"//span[.='提 交']/parent::button")
    # submit="//span[.='提 交']/parent::button"
    new_success_info=(By.XPATH,"//span[text()='新增科室成功']")
    query_success_info = (By.XPATH, "//td[text()='测试科室5527']")
    updata_success_info = (By.XPATH, "//span[text()='修改科室成功']")
    del_success_info = (By.XPATH, "//span[text()='删除成功']")
    def pubilc(self):
        # 点击基础管理
        self.move_click(self.basic_management)
        # 点击科室设置
        self.move_click(self.dept_management)
        time.sleep(3)
    #新增科室操作
    def newDept(self,name,deptcode,deptname,deptlevel):
        DeptPage.pubilc(self)
        # 输入科室名称
        self.input(self.name, name)
        # 点击查询
        self.move_click(self.query)
        time.sleep(2)
        flag=self.isElementExist(self.query_success_info)
        if flag:
            # 选择科室名称
            self.move_click(self.selectName1)
            # 点击删除
            self.move_click(self.delete)
            # 点击确定
            self.move_click(self.dete)
            time.sleep(1)
            #点击新增
            self.move_click(self.deptNew)
            #所属机构
            self.move_click(self.officeName)
            print("所属机构：",self.text(self.officeselect))
            #机构选择
            self.move_click(self.officeselect)
            #点击使用年限框
            self.move_click(self.yearsBox)
            print("使用年限：",self.text(self.years))
            #选择使用年限
            self.move_click(self.years)

            #点击是否启用框
            self.move_click(self.isEnable)
            print("是否启用:",self.text(self.Enable))
            #选择启用
            self.move_click(self.Enable)
            #输入科室编码
            self.input(self.deptCode,deptcode)
            print("科室编码:",deptcode)
            #输入科室名称
            self.input(self.deptName, deptname)
            print("科室名称：",deptname)
<<<<<<< HEAD
            #输入科室级别
            self.input(self.deptLevel,deptlevel)
            print("科室级别：",deptlevel)
=======
>>>>>>> gitee/master

            time.sleep(0.5)
            # 点击提交
            self.move_click(self.submit)
            time.sleep(2)
        else:
            # 点击新增
            self.move_click(self.deptNew)
            # 所属机构
            self.move_click(self.officeName)
            print("所属机构：", self.text(self.officeselect))
            # 机构选择
            self.move_click(self.officeselect)
            # 点击使用年限框
            self.move_click(self.yearsBox)
            print("使用年限：", self.text(self.years))
            # 选择使用年限
            self.move_click(self.years)
            # 点击是否启用框
            self.move_click(self.isEnable)
            print("是否启用:", self.text(self.Enable))
            # 选择启用
            self.move_click(self.Enable)
            # 输入科室编码
            self.input(self.deptCode, deptcode)
            print("科室编码:", deptcode)
            # 输入科室名称
            self.input(self.deptName, deptname)
            print("科室名称：", deptname)
<<<<<<< HEAD
            # 输入科室级别
            self.input(self.deptLevel, deptlevel)
            print("科室级别：", deptlevel)
=======
>>>>>>> gitee/master

            time.sleep(0.5)
            # 点击提交
            self.move_click(self.submit)
            time.sleep(2)

    #查询科室操作
    def queryDept(self,name):

        DeptPage.pubilc(self)
        #输入科室名称
        self.input(self.name,name)
        #点击查询
        self.move_click(self.query)
        time.sleep(2)

    # 修改科室操作

    def updataDept(self, name, deptname):
        DeptPage.queryDept(self, name)
        # 点击修改
        self.move_click(self.updata)
        # 清除科室名称
        self.move_click(self.deptName2)
        js = 'document.querySelector("#deptName").value="";'
        self.driver.execute_script(js)
        time.sleep(1)
        # 输入科室名称
        self.input(self.deptName2, deptname)
        print("要修改的科室：",deptname)
        # 点击提交
        self.move_click(self.submit)
        time.sleep(2)

    #删除科室操作
    def delDept(self,name):
        DeptPage.queryDept(self,name)
        print("要删除的科室：",self.text(self.delName))
        #选择科室名称
        self.move_click(self.selectName)
        #点击删除
        self.move_click(self.delete)
        #点击确定
        self.move_click(self.dete)
        time.sleep(2)

    #新增科室校验
    def get_new_success_msg(self):
        success_elem=self.wait_presence_element(self.new_success_info)
        return  success_elem.text
    #查询科室校验
    def get_query_success_msg(self):
        success_elem=self.wait_presence_element(self.query_success_info)
        return  success_elem.text

    #修改科室校验
    def get_updata_success_msg(self):
        success_elem=self.wait_presence_element(self.updata_success_info)
        return  success_elem.text

    #删除科室校验
    def get_del_success_msg(self):
        success_elem=self.wait_presence_element(self.del_success_info)
        return  success_elem.text


