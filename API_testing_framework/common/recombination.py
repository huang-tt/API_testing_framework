import os,sys
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)	#添加python项目的环境地址
sys.path.append("F:\Python\Lib\site-packages")#添加python项目的第三库的环境地址

#将上个接口返回的内容给下个接口使用
from utils.openrationExcel import *
import json

def recombination_data(excel,response):
    """
    通过“#”找出需要修改的参数
    :param excel: 需要修改的数据
    :param response: 拿到返回数据
    :return:
    """
    # print(excel, type(excel))
    new_excel = []
    for i in excel:
        # print("i的值{}".format(i),type(i))
        #将字符串转为字典
        case_datas = json.loads(i['case_data'])
        # print("case_datas的值{}".format(case_datas),type(case_datas))
        for j in case_datas.items():
            if j[1] == '#':
                # print(j[0])
                #将原来的“#”替换为返回的值
                case_datas[j[0]] = response[j[0]]
                # print(case_datas)
                # 将修改好的数据，重新赋值
                i['case_data'] = str(case_datas)
            else:
                pass
        new_excel.append(i)
    return new_excel











# s ={'success': True, 'object': {'code': '099789'}, 'message': '', 'code': '200', 'remark': '', 'time': '2020-12-24 17:11:37', 'addition': '', 'id': ''}
# recombination_data(excel,s)