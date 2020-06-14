from hamcrest import *
from jsonpath import jsonpath
from test_requests.test_label.base_api.label import Label
# from ..base_api.label import Label  # 相对导入，和上面等价


class TestLabel:
    # 获取token,token只需要每个用例集之前执行一次，不需要重复获取，所以用setup_class
    def setup_class(self):
        self.label = Label()  # 实例化Label类
        # 获取token，调用yaml_load方法，并传入需打开的文件，取其corpid和corpsecret的值
        self.token = self.label.get_token(self.label.yaml_load("./../data/config.yaml")["corpid"],
                                          self.label.yaml_load("./../data/config.yaml")["corpsecret"])
        self.data = self.label.yaml_load("./../data/testdata.yaml")

    # 创建标签，传入tagid
    def test_create_label_tagid(self):
        # r = self.label.create_label_tagid("Ui4", 4)  # 调用create_label_tagid方法并传入相应参数
        r = self.label.create_label_tagid(self.data["create_label_tagid"]["tagname"],
                                          self.data["create_label_tagid"]["tagid"])
        assert r["errcode"] == 0
        # jsonpath断言
        assert jsonpath(r, "$.errcode") == [0]
        # jsonschema断言，没有代理，没找到合适生成模板的jsonschema工具
        # hamcrest断言
        assert_that(r["errcode"], equal_to(0))

    # 创建标签，不传入tagid,不指定时则以目前最大的id自增
    def test_create_label(self):
        # r = self.label.create_label("Ui5")  # 调用create_label方法并传入相应参数
        r = self.label.create_label(self.data["create_label"]["tagname"])
        assert r["errcode"] == 0
        # jsonpath断言
        assert jsonpath(r, "$.errcode") == [0]
        # jsonschema断言，没有代理，没找到合适生成模板的jsonschema工具
        # hamcrest断言
        assert_that(r["errcode"], equal_to(0))

    # 更新标签名字
    def test_update_label(self):
        # r = self.label.update_label(4, "Ui4_edit")  # 调用update_label方法并传入相应参数
        r = self.label.update_label(self.data["update_label"]["tagid"], self.data["update_label"]["tagname"])
        assert r["errcode"] == 0
        # jsonpath断言
        assert jsonpath(r, "$.errcode") == [0]
        # jsonschema断言，没有代理，没找到合适生成模板的jsonschema工具
        # hamcrest断言
        assert_that(r["errcode"], equal_to(0))

    # 删除标签
    def test_delete_label(self):
        # r = self.label.delete_label(4)  # 调用delete_label方法并传入相应参数
        r = self.label.delete_label(self.data["delete_label"]["tagid"])
        assert r["errcode"] == 0
        # jsonpath断言
        assert jsonpath(r, "$.errcode") == [0]
        # jsonschema断言，没有代理，没找到合适生成模板的jsonschema工具
        # hamcrest断言
        assert_that(r["errcode"], equal_to(0))

    # 获取标签成员
    def test_get_labelmember(self):
        # r = self.label.get_labelmember(1)  # 调用get_labelmember方法并传入相应参数
        r = self.label.get_labelmember(self.data["get_labelmember"]["tagid"])
        assert r["errcode"] == 0
        # jsonpath断言
        assert "阿白" in jsonpath(r, "$..name")
        # jsonschema断言，没有代理，没找到合适生成模板的jsonschema工具
        # hamcrest断言
        assert_that(len(r["userlist"]), equal_to(3))

    # 增加标签成员,传入所有参数
    def test_create_labelmember(self):
        # r = self.label.create_labelmember_all(1, ["lisi", "lisi1"], [3, 4])  # 调用create_labelmember_all方法并传入相应参数
        r = self.label.create_labelmember_all(self.data["create_labelmember"]["tagid"],
                                              self.data["create_labelmember"]["userlist"],
                                              self.data["create_labelmember"]["partylist"])
        assert r["errcode"] == 0
        # jsonpath断言
        assert jsonpath(r, "$.errcode") == [0]
        # jsonschema断言，没有代理，没找到合适生成模板的jsonschema工具
        # hamcrest断言
        assert_that(r["errcode"], equal_to(0))

    # 增加标签成员,传userlist不传partylist
    def test_create_labelmember_userlist(self):
        # r = self.label.create_labelmember_userlist(1, ["secheng1", "secheng2"])  # 调用create_labelmember_userlist方法并传入相应参数
        r = self.label.create_labelmember_userlist(self.data["create_labelmember_userlist"]["tagid"],
                                                   self.data["create_labelmember_userlist"]["userlist"])
        assert r["errcode"] == 0
        # jsonpath断言
        assert jsonpath(r, "$.errcode") == [0]
        # jsonschema断言，没有代理，没找到合适生成模板的jsonschema工具
        # hamcrest断言
        assert_that(r["errcode"], equal_to(0))

    # 增加标签成员,不传userlist传partylist
    def test_create_labelmember_partylist(self):
        # r = self.label.create_labelmember_partylist(1, [2])  # 调用create_labelmember_partylist方法并传入相应参数
        r = self.label.create_labelmember_partylist(self.data["create_labelmember_partylist"]["tagid"],
                                                    self.data["create_labelmember_partylist"]["partylist"])
        assert r["errcode"] == 0
        # jsonpath断言
        assert jsonpath(r, "$.errcode") == [0]
        # jsonschema断言，没有代理，没找到合适生成模板的jsonschema工具
        # hamcrest断言
        assert_that(r["errcode"], equal_to(0))

    # 删除标签成员,传入所有参数
    def test_delete_labelmember_all(self):
        # r = self.label.delete_labelmember_all(1, ["lisi", "lisi1"], [3, 4])  # 调用delete_labelmember_all方法并传入相应参数
        r = self.label.delete_labelmember_all(self.data["delete_labelmember_all"]["tagid"],
                                              self.data["delete_labelmember_all"]["userlist"],
                                              self.data["delete_labelmember_all"]["partylist"])
        assert r["errcode"] == 0
        # jsonpath断言
        assert jsonpath(r, "$.errcode") == [0]
        # jsonschema断言，没有代理，没找到合适生成模板的jsonschema工具
        # hamcrest断言
        assert_that(r["errcode"], equal_to(0))

    # 删除标签成员,传userlist不传partylist
    def test_delete_labelmember_userlist(self):
        # r = self.label.delete_labelmember_userlist(1, ["secheng1", "secheng2"])  # 调用delete_labelmember_userlist方法并传入相应参数
        r = self.label.delete_labelmember_userlist(self.data["delete_labelmember_userlist"]["tagid"],
                                                   self.data["delete_labelmember_userlist"]["userlist"])
        assert r["errcode"] == 0
        # jsonpath断言
        assert jsonpath(r, "$.errcode") == [0]
        # jsonschema断言，没有代理，没找到合适生成模板的jsonschema工具
        # hamcrest断言
        assert_that(r["errcode"], equal_to(0))

    # 删除标签成员,不传userlist传partylist
    def test_delete_labelmember_partylist(self):
        # r = self.label.delete_labelmember_partylist(1, [2])  # 调用delete_labelmember_partylist方法并传入相应参数
        r = self.label.delete_labelmember_partylist(self.data["delete_labelmember_partylist"]["tagid"],
                                                    self.data["delete_labelmember_partylist"]["partylist"])
        assert r["errcode"] == 0
        # jsonpath断言
        assert jsonpath(r, "$.errcode") == [0]
        # jsonschema断言，没有代理，没找到合适生成模板的jsonschema工具
        # hamcrest断言
        assert_that(r["errcode"], equal_to(0))

    # 获取标签列表
    def test_get_labellist(self):
        r = self.label.get_labellist()  # 调用get_labellist方法
        assert r['errcode'] == 0
        # jsonpath断言
        res = jsonpath(r, "$.taglist[?(@.tagname)]['tagname']")[1]
        assert res == "Ui3"
        # jsonschema断言，没有代理，没找到合适生成模板的jsonschema工具
        # hamcrest断言
        assert_that(r["errcode"], equal_to(0))
