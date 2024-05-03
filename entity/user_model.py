# 用户实体类
class User:
    # 编号 主键ID
    id = None
    # 用户名
    name = None
    # 密码
    password = None
    # 用户类型
    type = None

    def __init__(self, username, password):
        self.name = username
        self.password = password

    # @staticmethod
    # def my_constructor(userName, password, newPassword):
    #     obj = User(userName, password)
    #     obj.newPassword = newPassword
    #     return obj
