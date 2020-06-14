import requests


class TestToken:
    # 获取access_token，通过params关键字来传递参数，规范写法
    def test_token1(self):
        params = {
            "corpid":"ww170e13c876c74789",
            "corpsecret":"N5-mHIhmaAYP1-qcMaccISC0Ktw5L8YY93GDjUy7pjs"
        }
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()['errcode'] == 0

    # 获取access_token，url带参传入,一般不采用这种方式，规范的写法是上面一种
    def test_token2(self):
        corpid = "ww170e13c876c74789"
        corpsecret = "N5-mHIhmaAYP1-qcMaccISC0Ktw5L8YY93GDjUy7pjs"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=url)
        print(r.json())
        assert r.json()['errcode'] == 0
