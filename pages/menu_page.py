
import time
from selenium.webdriver.common.by import By
from common.base_page import BasePage
class MenuPage(BasePage):
    #基础管理
    basic_management = (By.XPATH,"//*[contains(text(),'基础管理')]")
    #菜单管理
    menu_management = (By.XPATH, "//*[contains(text(),'菜单管理')]")
    """新增菜单"""
    #新增
    menuNew = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-background-ghost']")
    #菜单
    menu=(By.XPATH,"//span[text()='菜 单']")
    #系统名称
    systemName=(By.XPATH,"//ul[@class='ant-select-selection__rendered']")
    #选择系统
    systemChoice=(By.XPATH,"//span[@title='开发平台']")
    #菜单名称
    menuName = (By.ID, "menuName")
    #菜单URL
    path = (By.ID, "path")
    #组件地址
    component=(By.ID,"component")
    #是否隐藏
    isHide = (By.XPATH, "//div[@id='showFlag']//div[@class='ant-select-selection__rendered']")
    #显示
    display=(By.XPATH, "//li[text()='显示']")

    """查询菜单"""
    #名称
    name=(By.XPATH,"//label[@title='名称']/../following-sibling::div[1]//input")
    #查询
    query=(By.XPATH, "//span[text()='查 询']")

    """修改菜单"""
    #修改按钮
    updata = (By.XPATH, "//td[@class='ant-table-row-cell-break-word']//i[@title='修改']")
    #相关权限
    perms=(By.ID,"perms")
    #菜单排序
    orderNum=(By.XPATH,"//div[@id='orderNum']//input")

    """删除菜单"""
    # 菜单名称
    selectName = (By.XPATH, "(//span[text()='测试菜单5527']/../preceding-sibling::td[1]//span[@class='ant-checkbox'])[2]")
    delname=(By.XPATH,"(//span[text()='测试菜单5527'])[2]")
    # 删除
    delete = (By.XPATH, "//span[text()='删 除']")
    # 确定
    dete = (By.XPATH, "//span[text()='确 定']/parent::button[@class='ant-btn ant-btn-primary']")

    #提交
    # submit=(By.XPATH,"//span[text()='提 交']")
    submit=(By.XPATH,"//span[.='提 交']/parent::button")
    new_success_info=(By.XPATH,"//span[text()='新增菜单成功']")
    query_success_info = (By.XPATH, "(//span[text()='测试菜单5527'])[2]")
    updata_success_info = (By.XPATH, "//span[text()='修改菜单成功']")
    del_success_info = (By.XPATH, "//span[text()='删除成功']")

    #公共操作
    def public(self):
        # 点击基础管理
        self.move_click(self.basic_management)
        self.scroll(self.menu_management)
        # 点击菜单管理
        self.move_click(self.menu_management)
    #新增操作
    def newMenu(self,name,menuname,path,component):
        MenuPage.public(self)
        #输入名称
        self.input(self.name,name)
        #点击查询
        self.move_click(self.query)
        time.sleep(2)
        flag=self.isElementExist(self.query_success_info)
        if flag:
            # 选择菜单
            self.move_click(self.selectName)
            # 点击删除
            self.move_click(self.delete)
            # 点击确定
            self.move_click(self.dete)
            time.sleep(1)
            #点击新增
            self.move_click(self.menuNew)
            #点击菜单
            self.move_click(self.menu)
            # 点击系统名称框
            self.move_click(self.systemName)
            time.sleep(0.5)
            # 选择系统
            print("所属平台：", self.text(self.systemChoice))

            self.move_click(self.systemChoice)
            self.move_click(self.systemName)
            #输入菜单名称
            self.input(self.menuName,menuname)
            print("菜单名称：",menuname)
            #输入菜单URL
            self.input(self.path,path)
            print("菜单URL：",path)
            #输入组件地址
            self.input(self.component, component)
            print("组件地址：",component)
            #点击是否隐藏框
            self.move_click(self.isHide)
            time.sleep(0.5)
            print("是否隐藏：",self.text(self.display))
            #选择显示
            self.move_click(self.display)

            # 点击提交
            self.move_click(self.submit)
            time.sleep(1.5)
        else:
            # 点击新增
            self.move_click(self.menuNew)
            # 点击菜单
            self.move_click(self.menu)
            # 点击系统名称框
            self.move_click(self.systemName)
            time.sleep(0.5)
            # 选择系统
            print("所属平台：", self.text(self.systemChoice))

            self.move_click(self.systemChoice)
            self.move_click(self.systemName)
            # 输入菜单名称
            self.input(self.menuName, menuname)
            print("菜单名称：", menuname)
            # 输入菜单URL
            self.input(self.path, path)
            print("菜单URL：", path)
            # 输入组件地址
            self.input(self.component, component)
            print("组件地址：", component)
            # 点击是否隐藏框
            self.move_click(self.isHide)
            time.sleep(0.5)
            print("是否隐藏：", self.text(self.display))
            # 选择显示
            self.move_click(self.display)
            # 点击提交
            self.move_click(self.submit)
            time.sleep(1.5)

    #查询操作
    def queryMenu(self,name):
        MenuPage.public(self)
        #输入用户名
        self.input(self.name,name)
        #点击查询
        self.move_click(self.query)
        time.sleep(2)
    #修改操作
    def updataMenu(self,name,perms,ordernum):
        MenuPage.queryMenu(self,name)
        #点击修改
        self.move_click(self.updata)
        #输入相关权限
        self.input(self.perms,perms)
        print("相关权限：",perms)
        #输入菜单排序
        self.input(self.orderNum,ordernum)
        print("菜单排序：",ordernum)
        time.sleep(0.5)
        #点击提交
        self.move_click(self.submit)
        time.sleep(2.5)

    def delMenu(self,name):
        MenuPage.queryMenu(self,name)
        print("要删除的菜单：",self.text(self.delname))
        #选择菜单
        self.move_click(self.selectName)
        #点击删除
        self.move_click(self.delete)
        #点击确定
        self.move_click(self.dete)
        time.sleep(2.5)


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


