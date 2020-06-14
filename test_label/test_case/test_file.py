import yaml

# 怕yaml文件写错，可以生成一个yaml文件
class TestDemo:
    def test_token(self):
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
            yaml.dump(rep, f)  # 把rep里的内容写到config.yaml文件中