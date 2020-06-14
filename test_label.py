import requests


class TestLabel:
    # 获取token
    def setup(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid":"ww170e13c876c74789",
            "corpsecret":"N5-mHIhmaAYP1-qcMaccISC0Ktw5L8YY93GDjUy7pjs"
        }
        r = requests.get(url=url, params=params)
        # print(r.json())
        self.token = r.json()["access_token"]
        # print(self.token)

    # 创建标签
    def test_create_label(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/create"
        params = {
            "access_token":self.token
        }
        json = {
            "tagname": "Ui3",
            "tagid": 3
        }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 更新标签名字
    def test_update_label(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/update"
        params = {"access_token":self.token}
        json = {
            "tagid": 3,
            "tagname": "Ui3_edit"
        }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 删除标签
    def test_delete_label(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/delete"
        params = {
            "access_token":self.token,
            "tagid":3
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 获取标签成员
    def test_get_labelmember(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/get"
        params = {
            "access_token":self.token,
            "tagid":1
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 增加标签成员
    def test_create_labelmember(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers"
        params = {"access_token":self.token}
        json = {
            "tagid": 1,
            "userlist": ["lisi", "lisi1"],
            "partylist": [3,4]
        }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 删除标签成员
    def test_delete_labelmember(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers"
        params = {"access_token":self.token}
        json = {
            "tagid": 1,
            "userlist": ["lisi", "lisi1"],
            "partylist": [3,4]
        }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 获取标签列表
    def test_get_labellist(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/list"
        params = {"access_token":self.token}
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()['errcode'] == 0
