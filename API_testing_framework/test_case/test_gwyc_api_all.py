#参数化运行所有用例

import pytest
import json
import allure
import ast #将字符串转为字典
from utils.openrationExcel import *
from base.method import *
from common.login import *


@allure.feature('接口自动化测试用例')
@allure.story('登录')
@pytest.mark.parametrize('data', excel)
# @allure.title('测试1')

def test_gwyc_api(data):
    """
    调用接口
    :param data: 接口信息
    :return:
    """
    for i in data:
        data = i
        return data
    allure.dynamic.title(data['case_name'])
    # 对请求头做为空处理并添加token
    allure.step('获取headers')
    headers = data['case_headers']
    # 将字符串转化为字典
    headers = ast.literal_eval(headers)
    # print('----------------headers的值：', headers)
    # if len(str(headers).split()) ==0:
    #     pass
    # elif len(str(headers)) >=0:
    #     #转换为字典
    #     headers = json.loads(headers)
    #     #获取登录返回的token并添加到读取出来的headers里面
    #     headers['Authorization'] = company_login_token
    #     headers = headers

     # 对请求参数做为空处理
    params = data['case_data']
    if len(str(params).split()) == 0:
        pass
    elif len(str(params)) >= 0:
        params = params

    # 断言封装
    allure.step('断言验证')
    case_code = int(data['case_code'])

    def case_result_assert(r):
        assert r.json()['code'] == case_code  # 验证状态码
        assert data['case_result'] in json.dumps(r.json(), ensure_ascii=False)  # 验证响应数据

    # 执行用例
    allure.step('执行用例')
    if data['case_method'] == 'get':
        r = ApiRequst().send_requests(
            method='get',
            url=data['case_url'],
            data=params,
            headers=headers
        )
        case_result_assert(r=r)

    elif data['case_method'] == 'post':
        r = ApiRequst().send_requests(
            method='post',
            url=data['case_url'],
            data=json.loads(params),
            headers=headers
        )
        case_result_assert(r=r)










