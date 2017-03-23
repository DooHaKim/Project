# -*- coding: utf-8 -*-
import pymysql

def create_db_table(execute_str,db_name):
    db = pymysql.connect(host = 'localhost', user = 'root', passwd = 'pythonproject' ,db = db_name )
    cursor = db.cursor()
    cursor.execute(execute_str)
    db.commit()
    db.close()

def load_db_table(execute_str,db_name):
    db = pymysql.connect(host = 'localhost', user = 'django', passwd = 'djangoproject' ,db = db_name, )
    cursor = db.cursor()
    cursor.execute(execute_str)
    result_value = cursor.fetchall()
    db.close()
    return result_value
