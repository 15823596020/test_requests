from test_requests.test_label.base_api.baseapi import BaseApi


class WeWork(BaseApi):  # 继承BaseApi
    # 获取token
    def get_token(self, corpid, corpsecret):
        req = {
            "method":self.yaml_load("../data/config.yaml")["get_token"]["method"], #"get",
            "url":self.yaml_load("../data/config.yaml")["get_token"]["url"], #"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params":{"corpid":corpid, "corpsecret":corpsecret}
        }
        r = self.send_api(req)  # 调用send_api方法，并传入一个json结构体的请求信息
        self.token = r.json()["access_token"]  # 获取token的值
        return self.token  # 返回self.token