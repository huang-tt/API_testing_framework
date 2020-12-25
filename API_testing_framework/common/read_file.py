#封装读取文件的方法
import os,sys
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)	#添加python项目的环境地址
sys.path.append("F:\Python\Lib\site-packages")#添加python项目的第三库的环境地址
import os

#获取当前目录
os.path.dirname(__file__)
#获取当前目录的上一级目录
os.path.dirname(os.path.dirname(__file__))
#获取指定的目录
def fileDir(data):
    """

    :param data: 目录
    :return:
    """
    base_path = os.path.dirname(os.path.dirname((__file__)))
    #返回获取到的目录
    return os.path.join(base_path,data)

#获取路径下的文件
def filePath(fileDir="data",fileName="data.xlsx"):
    """

    :param fileDir: 目录
    :param fileName: 文件名称
    :return:
    """
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)

a=filePath()
print(a)

