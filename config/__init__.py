"""
配置文件
"""
import os


class Setting:
    #host 地址
    host='http://59.56.182.79:9192'

    #login_url
    login_url='/#/ygt'

    user='ceshi01'
    pwd='123456'

    #root_path 项目跟目录
    root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    #img_path 截图目录
    img_path=os.path.join(root_path,'img')
    if not os.path.exists(img_path):
        os.mkdir(img_path)