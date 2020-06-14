from test_requests.test_department.base_api.department import Department


class TestDepartment:
    # 获取token,token只需要每个用例集之前执行一次，不需要重复获取，所以用setup_class
    def setup_class(self):
        self.department = Department()  # 实例化Department
        # 获取token，调用yaml_load方法，并传入需打开的文件，取其corpid和corpsecret的值
        self.token = self.department.get_token(self.department.yaml_load("config.yaml")["corpid"],
                                               self.department.yaml_load("config.yaml")["corpsecret"])

    # 创建部门
    def test_create_department(self):
        # 调用create_department方法并传入相应参数
        r = self.department.create_department("重庆研发中心4", "CQYF4", 1, 4, 7)
        assert r["errcode"] == 0

    # 更新部门
    def test_update_department(self):
        # 调用update_department方法并传入相应参数
        r = self.department.update_department("重庆研发中心4_edit", "CQYF4", 1, 4, 7)
        assert r["errcode"] == 0

    # 删除部门
    def test_delete_department(self):
        # 调用delete_department方法并传入相应参数
        r = self.department.delete_department(7)
        assert r["errcode"] == 0

    # 获取某部门列表
    def test_get_departmentlist_id(self):
        # 调用get_departmentlist_id方法,需传入参数c_id，表示获取传入参数的相关部门信息
        r = self.department.get_departmentlist_id(6)
        assert r["errcode"] == 0

    # 获取所有部门列表
    def test_get_departmentlist(self):
        # 调用get_departmentlist方法，不需传入参数，表示获取所有的部门信息
        r = self.department.get_departmentlist()
        assert r["errcode"] == 0
