# 文件数据实体类
class FileData:
    # 编号 主键ID
    id = None
    # 标题
    title = None
    # 上传时间
    upload_date = None
    # 文件路径
    file_path = None
    # 描述
    description = None
    # 文件的名称
    file_name = None
    # 文件大小
    file_size = None
    # 文件类型
    type = None

    def __init__(self, title, upload_date, file_path, description, file_name, file_size, type):
        self.title = title
        self.upload_date = upload_date
        self.file_path = file_path
        self.description = description
        self.file_name = file_name
        self.file_size = file_size
        self.type = type

    # @staticmethod
    # def my_constructor(userName, password, newPassword):
    #     obj = User(userName, password)
    #     obj.newPassword = newPassword
    #     return obj
