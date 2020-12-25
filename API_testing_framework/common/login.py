#封装登录方法
import pytest
from base.method import *
# from utils.openrationExcel import *
# @putest.fixture装饰器整个模块运行前运行一次里面的方法
@pytest.fixture(scope='module')
def company_login_token():
    """获取token并返回"""
    url = "http://39.108.95.246:6218/bbox2-web-mobile-cat/clerk/loginForClerk"
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    data = {"code":"666666","phone":"13577777777","app_id":"6015","cj_type":0,"token":"TOKEN","user_id":"USER_ID"}
    r = requests.post(url=url,data=json.dumps(data),headers=headers)
    #返回所有token信息
    return r.json()

