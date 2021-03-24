from common.global_variable import Global_variable

new_menu_data_success=[
    {"name":"测试菜单5527","menuname":"测试菜单5527","path":"/ceshi","component":"PageView","expected":"新增菜单成功"}
]
query_menu_data_success=[
    {"name":"测试菜单5527","expected":"测试菜单5527"}
]
updata_menu_data_success=[
    {"name":"测试菜单5527","perms":"admin","orderum":"{}".format(Global_variable().ran),"expected":"修改菜单成功"}
]
del_menu_data_success=[
    {"name":"测试菜单5527","expected":"删除成功"}
]