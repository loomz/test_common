import requests
import json


# 定义一个common的类，它的父类是object
class CommonHttp(object):
    # common的构造函数
    def __init__(self, url_root):
        # 被测系统的根路由
        self.url_root = url_root

    # 封装你自己的get请求，uri是访问路由，params是get请求的参数，如果没有默认为空
    def get(self, uri, params=''):
        # 拼凑访问地址
        url = self.url_root + uri + params
        # 通过get请求访问对应地址
        res = requests.get(url)
        # 返回request的Response结果，类型为requests的Response类型
        return res

    # 封装你自己的post方法，uri是访问路由，params是post请求需要传递的参数，如果没有参数这里为空
    def post(self, uri, params=''):
        # 拼凑访问地址
        url = self.url_root + uri
        if len(params) > 0:
            # 如果有参数，那么通过post方式访问对应的url，并将参数赋值给requests.post默认参数data
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.post(url, data=params)
        else:
            # 如果无参数，访问方式如下
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.post(url)
        return res

        # 封装你自己的post方法，uri是访问路由，params是post请求需要传递的参数，如果没有参数这里为空

    def post_json(self, uri, params):
        # 拼凑访问地址
        url = self.url_root + uri
        if isinstance(params, dict):
            res = requests.post(url, json=params, headers={"Content-Type": "application/json; charset=UTF-8"})
        elif (isinstance(params, str)) and (len(params) > 0):
            print("json str")
            res = requests.post(url, data=json.dumps(params),
                                headers={"Content-Type": "application/json; charset=UTF-8"})
        else:
            # 如果无参数，访问方式如下
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.post(url)
        return res

    # url_params = {"access_token": access_token}
    def post_data(self, uri, url_params, data):
        url = self.url_root + uri
        data = json.dumps(data, ensure_ascii=False)
        response = requests.post(url,
                                 params=url_params,
                                 headers={'Content-Type': 'application/json; charset=UTF-8'},
                                 data=data.encode('utf-8'))
