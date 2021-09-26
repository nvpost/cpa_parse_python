def get_products(root_node, db):
    for offer in root_node.findall('shop/offers/offer'):
        productsArr = []
        product_id = offer.attrib['id']
        category_id = offer.find('categoryId').text

        name = offer.find('name').text

        try:
            description = offer.find('description').text
        except:
            description = ""

        oldprice = offer.find('oldprice').text if offer.find('oldprice') else " "

        price = offer.find('price').text
        url = offer.find('url').text
        vendor = offer.find('vendor').text
        picturesNodes = offer.findall('picture') if offer.findall('picture') else " "

        pictures = list(map(lambda p:p.text, picturesNodes))

        productsArr.append(
            (category_id, product_id, name, description, url, vendor, oldprice, price)
        )

        query = """INSERT INTO products(category_id, product_id, name, description, url, vendor, oldprice, price)
        values(%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor = db.cursor()
        cursor.executemany(query,productsArr)
        db.commit()