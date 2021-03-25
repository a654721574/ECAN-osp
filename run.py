import logging
import pytest

if __name__ == '__main__':
    pytest.main(['-q','./test_cases'])
    # logging.basicConfig(level=logging.DEBUG)
    # pytest.main(['-q','./test_cases/test_002_office.py','./test_cases/test_003_role.py',
    #              '-s','--alluredir','report/xml'])

    # pytest.main(['-q','./test_cases'])
    # pytest.main(['-q', './test_cases/test_001_login.py','./test_cases/test_002_office.py','./test_cases/test_003_role.py',
    #              '-s','--alluredir','report/xml'])


# allure serve report/xml