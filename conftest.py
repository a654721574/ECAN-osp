"""conftest.py 文件名称是固定的。

统一存放 fixture 的地方。
"""
import logging
import time

import pytest
from selenium import webdriver

#
@pytest.fixture(autouse=True)
def get_browser():


    # options = webdriver.ChromeOptions()
    # options.add_argument('--start-maximized')
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
    driver.maximize_window()
    # 设置隐式等待
    wait_timeout = 15
    driver.implicitly_wait(wait_timeout)
    yield driver
    time.sleep(1)
    driver.quit()

