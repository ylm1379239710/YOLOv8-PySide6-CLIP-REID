from entity.record_model import Record
from utils import db


def add_record(record: Record):
    """
    新增文件
    :param record: 任务记录实体
    :return: 新增成功返回插入数据id，登录失败，返回None
    """
    con = None
    try:
        con = db.getCon()
        cursor = con.cursor()
        query = (
            f"insert into record (title, time,type,detect_target,re_target,re_searched_target,result,result_path) values (%s, %s, %s, %s, %s, %s, %s, %s)")
        data = (record.title, record.time, record.type, record.detect_target, record.re_target,
                record.re_searched_target, record.result, record.result_path)
        cursor.execute(query, data)
        get_last_id_query = "SELECT LAST_INSERT_ID()"
        cursor.execute(get_last_id_query)
        last_id = cursor.fetchone()[0]
        return last_id
    except Exception as e:
        print(e)
        con.rollback()
        return None
    finally:
        db.closeCon(con)


def get_all_record():
    """
    查询所有记录
    :return: 查询成功返回所有记录，失败返回None
    """
    con = None
    try:
        con = db.getCon()
        cursor = con.cursor()
        cursor.execute(f"select id, title, time, type from record")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(e)
        con.rollback()
        return None
    finally:
        db.closeCon(con)


def delete_record_by_id(data_id):
    """
       删除记录
       :return: 删除成功无返回，失败返回None
       """
    con = None
    try:
        con = db.getCon()
        cursor = con.cursor()
        query = (f"delete from record where id = %s")
        cursor.execute(query, data_id)
    except Exception as e:
        print(e)
        con.rollback()
        return None
    finally:
        db.closeCon(con)


def search_record_by_condition(title, type):
    """
        根据条件查询文件
        :return: 查询成功返回符合条件数据，失败返回None
        """
    con = None
    try:
        con = db.getCon()
        cursor = con.cursor()
        if title != '':
            if type == "All":
                query = (f"select id, title, time, type from record where title like %s")
                cursor.execute(query, '%'+str(title)+'%')
            elif type == "Detect":
                query = (f"select id, title, time, type from record where title like %s and type = 'detect'")
                cursor.execute(query, '%'+str(title)+'%')
            else:
                query = (f"select id, title, time, type from record where title like %s and type = 're-identify'")
                cursor.execute(query, '%' + str(title) + '%')
        else:
            if type == "All":
                cursor.execute(f"select id, title, time, type from record")
            elif type == "Detect":
                cursor.execute(
                    f"select id, title, time, type from record where type = 'detect'")
            else:
                cursor.execute(
                    f"select id, title, time, type from record where type = 're-identify'")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(e)
        con.rollback()
        return None
    finally:
        db.closeCon(con)


def get_record_by_id(data_id):
    """
        根据id获取文件数据
        :return: 查询成功返回符合条件数据，失败返回None
        """
    con = None
    try:
        con = db.getCon()
        cursor = con.cursor()
        query = (f"select id, title, time , type, result, result_path from record where id = %s")
        cursor.execute(query, data_id)
        data = cursor.fetchone()
        return data
    except Exception as e:
        print(e)
        con.rollback()
        return None
    finally:
        db.closeCon(con)