import transliter

def get_params(root_node, db):
    cursor = db.cursor()
    paramsInsertArr = []
    for offer in root_node.findall('shop/offers/offer'):
        params = offer.findall('param')
        product_id = offer.attrib['id']
        for param in params:
            value = param.text
            name = param.attrib['name']
            prettyUrl = transliter.transliter(value)
            paramsInsertArr.append((product_id, name, value, prettyUrl))
    #     parentId = 0
    #     if 'parentId' in category.attrib:
    #         parentId = category.attrib['parentId']
    #     id = category.attrib['id']
    #
    #     text = category.text
    #
    #     prettyUrl = transliter.transliter(text)
    #
    #     categoryInsertArr.append((id, parentId, text, prettyUrl))
    #
    print(paramsInsertArr)

    query = """INSERT INTO params(product_id, name, value, pretty_url)
    values(%s, %s, %s, %s)
    """
    cursor.executemany(query,paramsInsertArr)
    db.commit()