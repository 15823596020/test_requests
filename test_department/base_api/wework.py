from test_requests.test_department.base_api.baseapi import BaseApi


class WeWork(BaseApi):
    # 获取token,需传入corpid, corpsecret参数
    def get_token(self, corpid, corpsecret):
        req = {
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params":{"corpid": corpid, "corpsecret": corpsecret}
        }
        r = self.send_api(req)
        self.token = r.json()["access_token"]
        return self.token

