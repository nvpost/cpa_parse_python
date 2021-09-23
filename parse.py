
import xml.etree.ElementTree as ET
import pymysql
import getCategory

from sql import sql

db = pymysql.connect(host="localhost", user="root", passwd="mysql", db=sql.db_name)

root_node = ET.parse('xml.xml').getroot()




# getCategory.get_gategory(root_node, db)
for offer in root_node.findall('shop/offers/offer'):
    id = offer.attrib['id']
    categoryId = offer.find('categoryId').text

    description = offer.find('description').text if offer.find('description') else " "

    name = offer.find('name').text

    oldprice = offer.find('oldprice').text if offer.find('oldprice') else " "

    price = offer.find('price').text
    url = offer.find('url').text
    vendor = offer.find('vendor').text if offer.find('vendor') else " "
    pictures = offer.find('picture').text if offer.find('picture') else " "

    print(id, categoryId, name, vendor)
