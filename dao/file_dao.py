from entity.file_model import FileData
from utils import db


def add_file_data(file: FileData):
    """
    新增文件
    :param file: 文件数据实体
    :return: 新增成功返回插入数据id，登录失败，返回None
    """
    con = None
    try:
        con = db.getCon()
        cursor = con.cursor()
        cursor.execute(f"insert into file (title, description,upload_date,file_path,file_name,file_size,type) VALUES ('{file.title}', '{file.description}', '{file.upload_date}', '{file.file_path}', '{file.file_name}', '{file.file_size}', '{file.type}')")
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


def get_all_file_data():
    """
    查询所有文件
    :return: 查询成功返回所有文件数据，失败返回None
    """
    con = None
    try:
        con = db.getCon()
        cursor = con.cursor()
        cursor.execute(f"select id, title, upload_date, type, description from file")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(e)
        con.rollback()
        return None
    finally:
        db.closeCon(con)

def delete_file_data_by_id(data_id):
    """
    删除文件
    :return: 删除成功无返回，失败返回None
    """
    con = None
    try:
        con = db.getCon()
        cursor = con.cursor()
        cursor.execute(f"delete from file where id = '{data_id}'")
    except Exception as e:
        print(e)
        con.rollback()
        return None
    finally:
        db.closeCon(con)

def search_data_by_condition(title,data_type):
    """
    根据条件查询文件
    :return: 查询成功返回符合条件数据，失败返回None
    """
    con = None
    try:
        con = db.getCon()
        cursor = con.cursor()
        if title != '':
            if data_type == "All":
                cursor.execute(f"select id, title, upload_date, type, description from file where title like '%{title}%'")
            elif data_type == "Video":
                cursor.execute(f"select id, title, upload_date, type, description from file where title like '%{title}%' and type in ('mp4','avi')")
            else:
                cursor.execute(f"select id, title, upload_date, type, description from file where title like '%{title}%' and type in ('jpg','jpeg','png','bmp')")
        else:
            if data_type == "All":
                cursor.execute(f"select id, title, upload_date, type, description from file")
            elif data_type == "Video":
                cursor.execute(f"select id, title, upload_date, type, description from file where type in ('mp4','avi')")
            else:
                cursor.execute(f"select id, title, upload_date, type, description from file where type in ('jpg','jpeg','png','bmp')")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(e)
        con.rollback()
        return None
    finally:
        db.closeCon(con)

def edit_by_id(id,title,description):
    """
    根据id编辑文件数据
    :return: 编辑成功无返回，失败返回None
    """
    con = None
    try:
        con = db.getCon()
        cursor = con.cursor()
        cursor.execute(f"update file set title = '{title}',description = '{description}' where id = '{id}'")
    except Exception as e:
        print(e)
        con.rollback()
        return None
    finally:
        db.closeCon(con)


def get_data_by_id(id):
    """
        根据id获取文件数据
        :return: 查询成功返回符合条件数据，失败返回None
        """
    con = None
    try:
        con = db.getCon()
        cursor = con.cursor()
        cursor.execute(f"select id, title, description, upload_date, file_path, file_name, file_size, type from file where id = '{id}'")
        data = cursor.fetchone()
        return data
    except Exception as e:
        print(e)
        con.rollback()
        return None
    finally:
        db.closeCon(con)
