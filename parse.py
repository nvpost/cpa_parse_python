
import xml.etree.ElementTree as ET
import pymysql
import getCategory
import getProducts
import getImg
import os

# TODO В качестве id использовать оригинальные ID для категорий и товаров
# TODO category = name

from sql import sql

db = pymysql.connect(host="localhost", user="root", passwd="mysql", db=sql.db_name)

root_node = ET.parse('xml.xml').getroot()


cursor = db.cursor()

getCategory.get_gategory(root_node, db)
# getProducts.get_products(root_node, db)

# getImg.get_img(root_node, db)

