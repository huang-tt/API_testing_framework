import os,sys
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)	#添加python项目的环境地址
sys.path.append("F:\Python\Lib\site-packages")#添加python项目的第三库的环境地址

import pytest
import json
import allure
import ast #将字符串转为字典
from utils.openrationExcel import excel
from base.method import *
from common.login import *
from common.assert_result import assert_content
from common.recombination import recombination_data


@allure.feature('接口自动化测试用例')
class Test_API():
    """
    接口自动化运行
    """

    @pytest.mark.parametrize('data', excel) #传入参数
    @allure.step('传入用例')    #设置用例步骤
    @allure.severity('blocker')     #设置用例严重级别为“中断缺陷”客户端程序无响应，无法执行下一步
    def test_gwyc_api(self,data):
        """
        调用接口
        :param data: 接口信息
        :return:
        """
        # for i in data:
        #     data = i
        #     return data

        allure.dynamic.story(data['case_module'])
        allure.dynamic.title(data['case_name'])

        # 对请求头做为空处理并添加token
        headers = data['case_headers']
        #将字符串转化为字典
        headers = ast.literal_eval(headers)


        # 对请求参数做为空处理
        params = data['case_data']
        if len(str(params).split()) == 0:
            pass
        elif len(str(params)) >= 0:
            params = params





        # 执行用例
        if data['case_method'] == 'get':
            r = ApiRequst().send_requests(
                method='get',
                url=data['case_url'],
                json=params,
                headers=headers
            )
            allure.attach("返回结果",'{0}'.format(r.json()))#在报告中显示返回结果
            assert int(r.json()['code']) == int(data['case_code'])   # 断言验证状态码
            a = assert_content(data['case_result'], r.json())   # 验证响应数据
            allure.attach("验证响应数据，{0}".format(a))


        elif data['case_method'] == 'post':
            r = ApiRequst().send_requests(
                method='post',
                url=data['case_url'],
                json=ast.literal_eval(params),
                headers=headers
            )

            allure.attach("返回结果",'{0}'.format(r.json()))
            assert int(r.json()['code']) == int(data['case_code'])  # 验证状态码
            allure.attach("验证响应数据，{0}".format(assert_content(data['case_result'], r.json())))# 验证响应数据
            #如果参数里面有“#”就可以通过此方法，去上个接口拿取到你想要的参数
            response = r.json()
            datas = recombination_data(excel, response)
            for data in datas:
                return data



