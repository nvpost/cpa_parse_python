import pymysql
import sql

db = pymysql.connect(host="localhost",user="root",passwd="mysql")
db_name = sql.dacha_depot

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
    id INT PRIMARY KEY NOT NULL,
    parent_id INT,
    category TEXT)"""
    cursor.execute(sql)
    db.commit()

def createProducts():
    db = pymysql.connect(host="localhost", user="root", passwd="mysql", db=db_name)
    cursor = db.cursor()
    sql = """CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY NOT NULL,
    category_id INT,
    name TEXT,
    description TEXT,
    url TEXT,
    vendor TEXT,
    oldprice TEXT,
    price INT)"""
    cursor.execute(sql)
    db.commit()

def createImg():
    db = pymysql.connect(host="localhost", user="root", passwd="mysql", db=db_name)
    cursor = db.cursor()
    sql = """CREATE TABLE IF NOT EXISTS img(
    id INT PRIMARY KEY NOT NULL auto_increment,
    product_id INT,
    src TEXT)"""
    cursor.execute(sql)
    db.commit()

createDb()
createCategory()
createProducts()
createImg()


# def createCategory():
#     db = pymysql.connect(host="localhost", user="root", passwd="mysql", db=db_name)
#     cursor = db.cursor()
#     sql = """CREATE TABLE IF NOT EXISTS Category(
#     id INT PRIMARY KEY NOT NULL auto_increment,
#     category_id INT,
#     parent_id INT,
#     category TEXT)"""
#     cursor.execute(sql)
#     db.commit()
#
# def createProducts():
#     db = pymysql.connect(host="localhost", user="root", passwd="mysql", db=db_name)
#     cursor = db.cursor()
#     sql = """CREATE TABLE IF NOT EXISTS Products(
#     id INT PRIMARY KEY NOT NULL auto_increment,
#     category_id INT,
#     product_id INT,
#     name TEXT,
#     description TEXT,
#     url TEXT,
#     vendor TEXT,
#     oldprice TEXT,
#     price INT)"""
#     cursor.execute(sql)
#     db.commit()
#
# def createImg():
#     db = pymysql.connect(host="localhost", user="root", passwd="mysql", db=db_name)
#     cursor = db.cursor()
#     sql = """CREATE TABLE IF NOT EXISTS img(
#     id INT PRIMARY KEY NOT NULL auto_increment,
#     product_id INT,
#     src TEXT)"""
#     cursor.execute(sql)
#     db.commit()