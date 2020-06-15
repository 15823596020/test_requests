import yaml

# 怕yaml文件写错，可以生成一个yaml文件
class TestDemo:
    # test_config方法生成config文件
    def test_config(self):
        rep = {
            "corpid": "ww170e13c876c74789",
            "corpsecret": "N5-mHIhmaAYP1-qcMaccISC0Ktw5L8YY93GDjUy7pjs",
            "create_label":{"method": "post", "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/create"},
            "update_label":{"method": "post", "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/update"},
            "delete_label":{"method": "get", "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/delete"},
            "get_labelmember":{"method": "get", "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/get"},
            "create_labelmember":{"method": "post", "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers"},
            "delete_labelmember":{"method": "post", "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers"},
            "get_labellist":{"method": "get", "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/list"}
        }
        with open("../data/config.yaml", "w") as f:
            yaml.dump(rep, f)  # 把rep里的内容写到config.yaml文件中

    # test_data方法生成测试数据
    def test_data(self):
        rep = {
            "create_label_tagid":{"tagname":"Ui4", "tagid":4},
            "create_label":{"tagname":"Ui5"},
            "update_label":{"tagid":4, "tagname":"Ui4_edit"},
            "delete_label":{"tagid":5},
            "get_labelmember":{"tagid":1},
            "create_labelmember":{"tagid":1,"userlist":["lisi", "lisi1"], "partylist":[3, 4]},
            "create_labelmember_userlist":{"tagid":1,"userlist":["secheng1", "secheng2"]},
            "create_labelmember_partylist":{"tagid":1, "partylist":[2]},
            "delete_labelmember_all":{"tagid":1,"userlist":["lisi", "lisi1"], "partylist":[3, 4]},
            "delete_labelmember_userlist":{"tagid":1,"userlist":["secheng1", "secheng2"]},
            "delete_labelmember_partylist":{"tagid":1, "partylist":[2]}
        }
        with open("../data/testdata.yaml", "w") as f:
            yaml.dump(rep, f)  # 把rep里的内容写到testdata.yaml文件中