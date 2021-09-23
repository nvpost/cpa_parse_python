import pymysql


db = pymysql.connect(host="localhost",user="root",passwd="mysql")
db_name = 'mydata'

cursor = db.cursor()


def createDb():
    try:
        sql = 'CREATE DATABASE '+db_name
        cursor.execute(sql)
    except:
        print("База существует")



def createCategory():
    db = pymysql.connect(host="localhost", user="root", passwd="mysql", db=db_name)
    cursor = db.cursor()
    sql = """CREATE TABLE IF NOT EXISTS Category(
    id INT PRIMARY KEY NOT NULL auto_increment,
    category_id INT,
    parent_id INT,
    category TEXT)"""
    cursor.execute(sql)
    db.commit()

createDb()
createCategory()