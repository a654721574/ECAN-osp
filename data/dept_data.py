from common.global_variable import Global_variable

new_dept_data_success=[
    {"name":"测试科室5527","deptcode":"{}".format(Global_variable().ran),"deptname":"测试科室5527",
     "deptlevel":"{}".format(Global_variable().ran),"expected":"新增科室成功"}
]

query_dept_data_success=[
    {"name":"测试科室5527","expected":"测试科室5527"}
]

updata_dept_data_success=[
    {"name":"测试科室5527","deptname":"测试科室5528","expected":"修改科室成功"}
]
del_dept_data_success=[
    {"name":"测试科室5528","expected":"删除成功"}
]