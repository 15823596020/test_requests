import yaml

# 怕yaml文件写错，可以生成一个yaml文件
class TestDemo:
    def test_token(self):
        rep = {
            "corpid": "ww170e13c876c74789",
            "corpsecret": "N5-mHIhmaAYP1-qcMaccISC0Ktw5L8YY93GDjUy7pjs"
        }
        with open("config.yaml", "w") as f:
            yaml.dump(rep, f)  # 把rep里的内容写到config.yaml文件中