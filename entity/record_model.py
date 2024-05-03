# 任务记录实体类
class Record:
    # 编号 主键ID
    id = None
    # 记录标题
    title = None
    # 记录时间
    time = None
    # 记录任务类型
    type = None
    # 结果路径
    result_path = None
    # 结果记录(针对重识别任务)
    result = None
    # 目标检测文件id(针对目标检测任务)
    detect_target = None
    # 重识别目标id(针对重识别任务)
    re_target = None
    # 重识别被检测对象id(针对重识别任务)
    re_searched_target = None

    def __init__(self, title, time, type, result_path, result, detect_target, re_target, re_searched_target):
        self.title = title
        self.time = time
        self.type = type
        self.result_path = result_path
        self.result = result
        self.detect_target = detect_target
        self.re_target = re_target
        self.re_searched_target = re_searched_target

    # @staticmethod
    # def my_constructor(userName, password, newPassword):
    #     obj = User(userName, password)
    #     obj.newPassword = newPassword
    #     return obj
