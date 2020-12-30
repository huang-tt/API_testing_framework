import os,sys
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)	#添加python项目的环境地址
sys.path.append("F:\Python\Lib\site-packages")#添加python项目的第三库的环境地址

#封装断言方法
import json #将字符串转为字典

def assert_content(case_assert,response):
    """
    断言对比
    :param case_assert: Excel中想要断言的结果
    :param response: 请求返回的结果
    :return:返回断言结果
    """
    fail_tent = ''
    #json.loads将字符串转换为字典
    case_result =json.loads(case_assert)
    for t in case_result.items():
        if t not in response.items():
            fail_tent += '{0}接口返回结果没有此值：{1},'.format(response,t)
        else:
            fail_tent += '断言结果成功'
    return fail_tent

# a = '{"a":2}'
# b = {'a':1,'b':2}
# print(assert_content(a,b))
