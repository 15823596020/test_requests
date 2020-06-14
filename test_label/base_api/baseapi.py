import requests
import yaml


class BaseApi:
    # send_api方法，传入的参数是一个字典,主要是封装requests.request
    def send_api(self, req):
        """
        1. 先把请求信息转化为一个json结构体
        2. 在base_api里面对requests.request进行封装
        3. 传入为json结构体的请求信息，给requests.request，
        使用关键字传参的方式传入的时候要注意解包
        :param req: 一个json结构体的请求信息
        :return:
        """
        # 两个**代表对字典进行解包，使用 K=V 的形式进行传参
        return requests.request(**req)

    # yaml_load方法用于打开传入的文件内容,主要是封装yaml
    def yaml_load(self, file):
        return yaml.safe_load(open(file))  # 返回打开的文件