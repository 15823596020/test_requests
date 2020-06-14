from test_requests.test_label.base_api.wework import WeWork


class Label(WeWork): # 继承WeWork类
    #  创建标签，create_label_tagid方法，需传入参数tagname, tagid
    def create_label_tagid(self, tagname, tagid):
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/create",
            "params": {"access_token": self.token},
            "json":{"tagname": tagname, "tagid": tagid}
        }
        r = self.send_api(req)  # 调用send_api方法，并传入一个json结构体的请求信息
        print(r.json())
        return r.json()  # 返回r.json()

    #  创建标签，create_label方法，需传入参数tagname；不传入tagid，因为tagid不是必填项，不指定时则以目前最大的id自增
    def create_label(self, tagname):
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/create",
            "params": {"access_token": self.token},
            "json": {"tagname": tagname}
        }
        r = self.send_api(req)  # 调用send_api方法，并传入一个json结构体的请求信息
        print(r.json())
        return r.json()  # 返回r.json()

    # 更新标签名字，update_label方法，需传入参数tagid, tagname
    def update_label(self, tagid, tagname):
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/update",
            "params": {"access_token": self.token},
            "json": {"tagid": tagid, "tagname": tagname}
        }
        r = self.send_api(req)  # 调用send_api方法，并传入一个json结构体的请求信息
        print(r.json())
        return r.json()  # 返回r.json()

    # 删除标签，delete_label方法，需传入参数tagid
    def delete_label(self, tagid):
        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/delete",
            "params": {"access_token": self.token, "tagid": tagid}
        }
        r = self.send_api(req)  # 调用send_api方法，并传入一个json结构体的请求信息
        print(r.json())
        return r.json()  # 返回r.json()

    # 获取标签成员，get_labelmember方法，需传入参数tagid
    def get_labelmember(self, tagid):
        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/get",
            "params": {"access_token": self.token, "tagid": tagid}
        }
        r = self.send_api(req)  # 调用send_api方法，并传入一个json结构体的请求信息
        print(r.json())
        return r.json()  # 返回r.json()

    # 增加标签成员，create_labelmember_all方法，需传入参数tagid,userlist,partylist
    def create_labelmember_all(self,tagid,userlist,partylist):
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers",
            "params": {"access_token": self.token},
            "json" : {"tagid": tagid,"userlist": userlist,"partylist": partylist}
        }
        r = self.send_api(req)  # 调用send_api方法，并传入一个json结构体的请求信息
        print(r.json())
        return r.json()  # 返回r.json()

    # 增加标签成员，create_labelmember_userlist方法，需传入参数tagid,userlist
    def create_labelmember_userlist(self, tagid, userlist):
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers",
            "params": {"access_token": self.token},
            "json": {"tagid": tagid, "userlist": userlist}
        }
        r = self.send_api(req)  # 调用send_api方法，并传入一个json结构体的请求信息
        print(r.json())
        return r.json()  # 返回r.json()

    # 增加标签成员，create_labelmember_partylist方法，需传入参数tagid,partylist
    def create_labelmember_partylist(self, tagid, partylist):
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers",
            "params": {"access_token": self.token},
            "json": {"tagid": tagid, "partylist": partylist}
        }
        r = self.send_api(req)  # 调用send_api方法，并传入一个json结构体的请求信息
        print(r.json())
        return r.json()  # 返回r.json()

    # 删除标签成员，delete_labelmember_all方法，需传入参数tagid,userlist,partylist
    def delete_labelmember_all(self,tagid,userlist,partylist):
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers",
            "params": {"access_token": self.token},
            "json": {"tagid": tagid, "userlist": userlist, "partylist": partylist}
        }
        r = self.send_api(req)  # 调用send_api方法，并传入一个json结构体的请求信息
        print(r.json())
        return r.json()  # 返回r.json()

    # 删除标签成员，delete_labelmember_userlist方法，需传入参数tagid,userlist
    def delete_labelmember_userlist(self, tagid, userlist):
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers",
            "params": {"access_token": self.token},
            "json": {"tagid": tagid, "userlist": userlist}
        }
        r = self.send_api(req)  # 调用send_api方法，并传入一个json结构体的请求信息
        print(r.json())
        return r.json()  # 返回r.json()

    # 删除标签成员，delete_labelmember_partylist方法，需传入参数tagid,partylist
    def delete_labelmember_partylist(self, tagid, partylist):
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers",
            "params": {"access_token": self.token},
            "json": {"tagid": tagid, "partylist": partylist}
        }
        r = self.send_api(req)  # 调用send_api方法，并传入一个json结构体的请求信息
        print(r.json())
        return r.json()  # 返回r.json()

    # 获取标签列表，get_labellist方法
    def get_labellist(self):
        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/list",
            "params": {"access_token": self.token},
        }
        r = self.send_api(req)  # 调用send_api方法，并传入一个json结构体的请求信息
        print(r.json())
        return r.json()  # 返回r.json()