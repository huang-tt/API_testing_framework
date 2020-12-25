import os,sys
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)	#添加python项目的环境地址
sys.path.append("F:\Python\Lib\site-packages")#添加python项目的第三库的环境地址

#封装读取文件方法
import xlrd
from common.read_file import *

class OperationExcel(object):
    #获取sheet表
    def getSheet(self):
        #打开Excel文件
        book = xlrd.open_workbook(filePath())

        #根据索引获取sheet表
        return book.sheet_by_index(0)


    #以列表形式读取出所有数据
    def getExcelDATAS(self):
        data = []
        #获取第一行
        # title = self.getSheet().row_values(0)
        #将第一行改为英文
        title = firstline.values()
        # print(title)
        #从第二行开始循环读取
        for row in range(1,self.getSheet().nrows):
            #获取每一行的内容
            row_value = self.getSheet().row_values(row)
            #将读取出来的每个用例作为一个字典添加到data列表
            data.append(dict(zip(title,row_value)))
        # for i in data:
        #     data = i

        return data





#对Excel第一行进行更改
firstline = {
    '用例ID': 'case_id',
    '用例模块': 'case_module',
    '用例名称': 'case_name',
    '用例地址': 'case_url',
    '请求方式': 'case_method',
    '请求类型': 'case_type',
    '请求参数': 'case_data',
    '请求头': 'case_headers',
    '前置条件': 'case_preposition',
    '是否执行': 'case_isRun',
    '状态码': 'case_code',
    '期望结果': 'case_result'
}



excel = OperationExcel().getExcelDATAS()
for i in excel:
    data = i

# print(excel)
# print(data)


# print(excel)

