from entity.user_model import User
from utils import db

# 记录当前用户名
currentUser: User = None


def login(user: User):
    """
    用户登录判断
    :param user: 用户实体
    :return: 登录成功返回用户信息实体，登录失败，返回None
    """
    con = None
    try:
        con = db.getCon()
        cursor = con.cursor()
        query = (f"select * from user where name= %s and password= %s")
        data = (user.name, user.password)
        cursor.execute(query, data)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        con.rollback()
        return None
    finally:
        db.closeCon(con)

# def modifyPassword(user: User):
#     """
#     修改密码
#     :param user: 用户实体
#     :return: 返回执行的记录条数
#     """
#     con = None
#     try:
#         con = db.getCon()
#         cursor = con.cursor()
#         cursor.execute(
#             f"update t_user set password='{user.newPassword}' where userName='{user.name}'")
#         return cursor.rowcount
#     except Exception as e:
#         print(e)
#         con.rollback()
#         return None
#     finally:
#         db.closeCon(con)
