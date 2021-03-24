
import time
from selenium.webdriver.common.by import By
from common.base_page import BasePage
class RolePage(BasePage):

    #基础管理
    basic_management = (By.XPATH,"//*[contains(text(),'基础管理')]")
    #角色管理
    roles = (By.XPATH, "//*[contains(text(),'角色管理')]")
    """新增角色"""
    #新增
    roleNew = (By.XPATH, "//span[.='新 增']/parent::button")
    #系统名称
    systemName=(By.XPATH,"//ul[@class='ant-select-selection__rendered']")
    #选择系统
    systemChoice=(By.XPATH,"//span[@title='开发平台']")
    #机构框
    officeFrame=(By.XPATH,"//span[@id='officeId']//span[@class='ant-select-selection__placeholder']")
    #机构搜索框
    officeSearchBox=(By.XPATH,"//span[@class='ant-select-dropdown-search']//input")
    #机构名称
    officeName = (By.XPATH, "//li[@class='filter-node']")
    #角色名称
    roleName=(By.ID,"roleName")
    #角色类型框
    roleTypeBox=(By.XPATH,"//div[text()='请选择角色类型']")
    #角色类型
    roleType=(By.XPATH,"//li[text()='业务系统角色']")
    #数据范围框
    dataRangeBox = (By.XPATH, "//div[text()='请选择数据范围']")
    #数据范围
    dataRange=(By.XPATH,"//li[text()='按明细设置']")
    #状态框
    stateBox=(By.XPATH,"//div[@id='status']/div/div")
    #状态
    state=(By.XPATH,"//li[text()='正常']")
    #权限选择
    #三角形基础管理
    basicTriangle=(By.XPATH,"//span[@title='基础管理']/preceding-sibling::span[2]")
    #基础管理
    basicManagement=(By.XPATH,"//span[@title='基础管理']/preceding-sibling::span[1]")
    #仓库管理
    warehouseManagement=(By.XPATH,"//span[@title='仓库管理']/preceding-sibling::span[1]")
    #三角形用户管理
    userTriangle=(By.XPATH,"//span[@title='用户管理']/preceding-sibling::span[2]")
    #用户管理
    userManagement=(By.XPATH,"//span[@title='用户管理']/preceding-sibling::span[1]")
    #删除用户
    delUser=(By.XPATH,"//span[@title='删除用户']/preceding-sibling::span[1]")
    #修改用户
    updateUser=(By.XPATH,"//span[@title='修改用户']/preceding-sibling::span[1]")
    #密码重置
    passwordReset=(By.XPATH,"//span[@title='密码重置']/preceding-sibling::span[1]")
    #导出Excel
    # exportExcel=(By.XPATH,"//span[@title='导出Excel']/preceding-sibling::span[1]")
    #新增用户
    newUser=(By.XPATH,"//span[@title='新增用户']/preceding-sibling::span[1]")
    #三角形角色管理
    roleTriangle=(By.XPATH,"//span[@title='角色管理']/preceding-sibling::span[2]")
    #角色管理
    roleManagement=(By.XPATH,"//span[@title='角色管理']/preceding-sibling::span[1]")
    #删除角色
    delRole=(By.XPATH,"//span[@title='删除角色']/preceding-sibling::span[1]")
    #修改角色
    updateRole=(By.XPATH,"//span[@title='修改角色']/preceding-sibling::span[1]")
    #新增角色
    newRole1=(By.XPATH,"//span[@title='新增角色']/preceding-sibling::span[1]")
    #三角形组织机构设置
    officeTriangl=(By.XPATH,"//span[@title='组织机构设置']/preceding-sibling::span[2]")
    #组织机构设置
    officeManagement=(By.XPATH,"//span[@title='组织机构设置']/preceding-sibling::span[1]")
    #删除部门
    delOffice=(By.XPATH,"//span[@title='删除部门']/preceding-sibling::span[1]")
    #新增部门
    newOffice=(By.XPATH,"//span[@title='新增部门']/preceding-sibling::span[1]")
    #修改部门
    updateOffice=(By.XPATH,"//span[@title='修改部门']/preceding-sibling::span[1]")
    #科室设置
    deptManagement=(By.XPATH,"//span[@title='科室设置']/preceding-sibling::span[1]")
    #数据域机构
    #部门
    office=(By.XPATH,"//span[@class='ant-form-item-children']/ul//span[@title='自动化测试(勿删)']/preceding-sibling::span[1]")
    """查询角色"""
    name=(By.XPATH,"(//label[text()='角色']/../following-sibling::div[1]//input)[1]")
    # 查询
    query = (By.XPATH, "//span[text()='查 询']")
    """修改角色"""
    updata = (By.XPATH, "//td[@class='ant-table-row-cell-break-word']//i[@title='修改角色']")
    roledDescribe = (By.ID, "remark")

    """删除角色"""
    # 角色名称
    selectName = (By.XPATH, "//td[text()='测试角色5527']/preceding-sibling::td[1]//span[@class='ant-checkbox']")
    delName=(By.XPATH,"//td[text()='测试角色5527']")
    # 删除
    delete = (By.XPATH, "//span[text()='删 除']")
    # 确定
    dete = (By.XPATH, "//span[text()='确 定']/parent::button[@class='ant-btn ant-btn-primary']")
    #提交
    submit=(By.XPATH,"//span[.='提 交']/parent::button")

    new_success_info=(By.XPATH,"//span[text()='新增角色成功']")
    query_success_info = (By.XPATH, "//td[text()='测试角色5527']")
    updata_success_info = (By.XPATH, "//span[text()='修改角色成功']")
    del_success_info = (By.XPATH, "//span[text()='删除成功']")

    #公共操作
    def public(self):
        # 点击基础管理
        self.move_click(self.basic_management)
        # 点击角色管理
        self.move_click(self.roles)
    #新增操作
    def newRole(self,name,officename,rolename):
        RolePage.public(self)
        # 输入角色
        self.input(self.name, name)

        # 点击查询
        self.move_click(self.query)
        time.sleep(2)
        #判断角色是否存在
        flag = self.isElementExist(self.query_success_info)
        if flag:
            # 选中角色名称
            self.move_click(self.selectName)
            # 点击删除
            self.move_click(self.delete)
            # 点击确定
            self.move_click(self.dete)
            time.sleep(0.5)
            #点击新增
            self.move_click(self.roleNew)
            # 点击系统名称框
            self.move_click(self.systemName)
            time.sleep(0.5)
            # 选择系统
            print("所属平台：", self.text(self.systemChoice))

            self.move_click(self.systemChoice)
            self.move_click(self.systemName)
            #点击机构框
            self.move_click(self.officeFrame)
            #输入机构名称
            self.input(self.officeSearchBox,officename)
            #选择机构名称
            self.move_click(self.officeName)
            print("机构名称：",officename)
            #输入角色名称
            self.input(self.roleName,rolename)
            print("角色名称：",rolename)
            #点击角色类型框
            self.move_click(self.roleTypeBox)
            #选择角色类型
            self.move_click(self.roleType)
            # time.sleep(0.5)
            print("角色类型:",self.text(self.roleType))
            #点击数据范围框
            self.move_click(self.dataRangeBox)
            #选择数据范围
            self.move_click(self.dataRange)
            # time.sleep(0.5)
            print("数据范围:", self.text(self.dataRange))
            #点击状态框
            self.move_click(self.stateBox)
            #选择状态
            self.move_click(self.state)
            print("状态：", self.text(self.state))
            # #点击三角形基础管理
            # self.move_click(self.basicTriangle)
            # #选择基础管理
            # self.move_click(self.basicManagement)
            # #选择仓库管理
            # self.move_click(self.warehouseManagement)
            # #点击三角形用户管理
            # self.move_click(self.userTriangle)
            # #选择用户管理
            # self.move_click(self.userManagement)
            #
            # #选择删除用户
            # self.move_click(self.delUser)
            # #选择修改用户
            # self.move_click(self.updateUser)
            # self.scroll(self.userTriangle)
            # #选择密码重置
            # self.move_click(self.passwordReset)
            # #选择新增用户
            # self.move_click(self.newUser)
            #
            # #再点击三角形用户管理
            # self.move_click(self.userTriangle)
            # #点击三角形角色管理
            # self.move_click(self.roleTriangle)
            # #选择角色管理
            # self.move_click(self.roleManagement)
            # #选择删除角色
            # self.move_click(self.delRole)
            # #选择修改角色
            # self.move_click(self.updateRole)
            # #选择新增角色
            # self.move_click(self.newRole1)
            # #再点击三角形角色管理
            # self.move_click(self.roleTriangle)
            # # 点击三角形组织机构设置
            # self.move_click(self.officeTriangl)
            # #选择组织机构设置
            # self.move_click(self.officeManagement)
            # #选择删除部门
            # self.move_click(self.delOffice)
            # #选择新增部门
            # self.move_click(self.newOffice)
            # #选择修改部门
            # self.move_click(self.updateOffice)
            # #选择科室设置
            # self.move_click(self.deptManagement)
            # # 点击三角形组织机构设置
            # self.move_click(self.officeTriangl)
            # self.scroll(self.office)
            # time.sleep(0.5)
            # #选择部门
            # self.move_click(self.office)
            time.sleep(0.5)
            # 点击提交
            self.move_click(self.submit)
            time.sleep(2)
        else:
            # 点击新增
            self.move_click(self.roleNew)
            # 点击系统名称框
            self.move_click(self.systemName)
            time.sleep(0.5)
            # 选择系统
            print("所属平台：", self.text(self.systemChoice))

            self.move_click(self.systemChoice)
            self.move_click(self.systemName)
            # 点击机构框
            self.move_click(self.officeFrame)
            # 输入机构名称
            self.input(self.officeSearchBox, officename)
            # 选择机构名称
            self.move_click(self.officeName)
            print("机构名称：", officename)
            # 输入角色名称
            self.input(self.roleName, rolename)
            print("角色名称：", rolename)
            # 点击角色类型框
            self.move_click(self.roleTypeBox)
            # 选择角色类型
            self.move_click(self.roleType)
            # time.sleep(0.8)
            print("角色类型:", self.text(self.roleType))
            # 点击数据范围框
            self.move_click(self.dataRangeBox)
            # 选择数据范围
            self.move_click(self.dataRange)
            # time.sleep(0.8)
            print("数据范围:", self.text(self.dataRange))
            # 点击状态框
            self.move_click(self.stateBox)
            # 选择状态
            self.move_click(self.state)
            print("状态：", self.text(self.state))
            # # 点击三角形基础管理
            # self.move_click(self.basicTriangle)
            # # 选择基础管理
            # self.move_click(self.basicManagement)
            # # 选择仓库管理
            # self.move_click(self.warehouseManagement)
            # # 点击三角形用户管理
            # self.move_click(self.userTriangle)
            # # 选择用户管理
            # self.move_click(self.userManagement)
            #
            # # 选择删除用户
            # self.move_click(self.delUser)
            # # 选择修改用户
            # self.move_click(self.updateUser)
            # self.scroll(self.userTriangle)
            # # 选择密码重置
            # self.move_click(self.passwordReset)
            # # 选择新增用户
            # self.move_click(self.newUser)
            #
            # # 再点击三角形用户管理
            # self.move_click(self.userTriangle)
            # # 点击三角形角色管理
            # self.move_click(self.roleTriangle)
            # # 选择角色管理
            # self.move_click(self.roleManagement)
            # # 选择删除角色
            # self.move_click(self.delRole)
            # # 选择修改角色
            # self.move_click(self.updateRole)
            # # 选择新增角色
            # self.move_click(self.newRole1)
            # # 再点击三角形角色管理
            # self.move_click(self.roleTriangle)
            # # 点击三角形组织机构设置
            # self.move_click(self.officeTriangl)
            # # 选择组织机构设置
            # self.move_click(self.officeManagement)
            # # 选择删除部门
            # self.move_click(self.delOffice)
            # # 选择新增部门
            # self.move_click(self.newOffice)
            # # 选择修改部门
            # self.move_click(self.updateOffice)
            # # 选择科室设置
            # self.move_click(self.deptManagement)
            # # 点击三角形组织机构设置
            # self.move_click(self.officeTriangl)
            # self.scroll(self.office)
            # time.sleep(0.5)
            # # 选择部门
            # self.move_click(self.office)
            time.sleep(0.5)
            # 点击提交
            self.move_click(self.submit)
            time.sleep(2)

    #查询操作
    def queryRole(self,name):
        RolePage.public(self)
        #输入角色
        self.input(self.name,name)
        #点击查询
        self.move_click(self.query)
        time.sleep(2)
    #修改操作
    def updata_Role(self,name,roleescribe):
        RolePage.queryRole(self,name)
        #点击修改
        self.move_click(self.updata)
        time.sleep(1)

        # 输入角色描述
        self.input(self.roledDescribe, roleescribe)
        print("修改角色描述",roleescribe)
        time.sleep(0.5)
        # 点击提交
        self.move_click(self.submit)
        time.sleep(1.5)

    def del_Role(self,name):
        RolePage.queryRole(self,name)
        print("要删除的角色：",self.text(self.delName))
        #选中角色名称
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

    #修改检验
    def get_updata_success_msg(self):
        success_elem=self.wait_presence_element(self.updata_success_info)
        return  success_elem.text
    #删除检验
    def get_del_success_msg(self):
        success_elem=self.wait_presence_element(self.del_success_info)
        return  success_elem.text

