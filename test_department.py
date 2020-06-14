import requests


class TestDepartment:
    # 获取token
    def setup(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid":"ww170e13c876c74789",
            "corpsecret":"N5-mHIhmaAYP1-qcMaccISC0Ktw5L8YY93GDjUy7pjs"
        }
        r = requests.get(url=url,params=params)
        # print(r.json())
        self.token = r.json()["access_token"]
        # print(self.token)

    # 创建部门
    def test_create_department(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        params = {
            "access_token":self.token
        }
        json = {
            "name":"重庆研发中心1",
            "name_en":"CQYF1",
            "parentid":1,
            "order":3,
            "id":4
        }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 更新部门
    def test_update_department(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        params = {
            "access_token": self.token
        }
        json = {
            "name": "重庆研发中心1_edit",
            "name_en": "CQYF1",
            "parentid":1,
            "order":3,
            "id":4
        }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 删除部门
    def test_delete_department(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        params = {
            "access_token":self.token,
            "id":4
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 获取部门列表
    def test_get_departmentlist(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        params = {
            "access_token": self.token,
            "id": 1
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()["errcode"] == 0