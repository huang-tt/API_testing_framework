import pytest

#生成allure报告
if __name__ == '__main__':
    """执行并生成allure报告"""
    # pytest.main(["-s","-v",'test_case/test_gwyc_api_all.py','--alluredir','./report/result'])
    pytest.main(["-s", "-v", 'test_case/test_api.py', '--alluredir', './report/result'])
    import os
    #读取json文件并生成HTML报告
    os.system('allure generate ./report/result -o ./report/html --clean')