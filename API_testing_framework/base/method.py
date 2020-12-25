#封装请求方式和请求方法

import requests
import json


class ApiRequst(object):
    #封装requests库下面的request方法
    def send_requests(self,method,url,data=None,params=None,headers=None,cookies=None,json=None,
                      files=None,auth=None,timeout=None,proxies=None,verify=None,cert=None):
        """

        :param method: 请求方法
        :param url: 请求地址
        :param data: 传输报文，可以是dict也可以是str,当没有指定hesders时，根据文本本身来
        :param params:只在get请求中使用，url后面的参数
        :param headers:请求头
        :param cookies:本地缓存，webd网页端
        :param json:传输报文，不管json是str还是dict，如果不指定headers中的content-type，默认为application/json
        :param files:上传文件
        :param auth:认证
        :param timeout:超时，为防止服务器不能及时响应
        :param proxies:代理
        :param verify:将verify设置为False后,取消警告的方式
        :param cert:证书
        :return:
        """
        self.r = requests.request(method=method,url=url,data=data,params=params,headers=headers,cookies=cookies,
                                  json=json,files=files,auth=auth,timeout=timeout,proxies=proxies,verify=verify,
                                  cert=cert)
        return self.r