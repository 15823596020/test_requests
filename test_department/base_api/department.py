from test_requests.test_department.base_api.wework import WeWork


class Department(WeWork):
     # create_department方法，需传入参数name, name_en, parentid, order, c_id
    def create_department(self, name, name_en, parentid, order, c_id):
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/create",
            "params": {"access_token": self.token},
            "json" : {"name": name, "name_en": name_en, "parentid": parentid, "order": order, "id": c_id}
        }
        # 调用send_api方法并传入字典req
        r = self.send_api(req)
        print(r.json())
        return r.json()

    # update_department方法，需传入参数name, name_en, parentid, order, c_id
    def update_department(self, name, name_en, parentid, order, c_id):
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/update",
            "params": {"access_token": self.token},
            "json": {"name": name, "name_en": name_en, "parentid": parentid, "order": order, "id": c_id}
        }
        # 调用send_api方法并传入字典req
        r = self.send_api(req)
        print(r.json())
        return r.json()

    # delete_department方法，需传入参数c_id
    def delete_department(self, c_id):
        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/delete",
            "params": {"access_token":self.token, "id":c_id}
        }
        # 调用send_api方法并传入字典req
        r = self.send_api(req)
        print(r.json())
        return r.json()

    # get_departmentlist_id方法，需传入参数c_id，表示获取传入参数的相关部门信息
    def get_departmentlist_id(self, c_id):
        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
            "params": {"access_token": self.token, "id": c_id}
        }
        # 调用send_api方法并传入字典req
        r = self.send_api(req)
        print(r.json())
        return r.json()

    # get_departmentlist方法，不需传入参数，表示获取所有的部门信息
    def get_departmentlist(self):
        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
            "params": {"access_token": self.token}
        }
        # 调用send_api方法并传入字典req
        r = self.send_api(req)
        print(r.json())
        return r.json()