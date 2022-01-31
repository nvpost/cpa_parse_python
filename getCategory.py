import transliter

def get_gategory(root_node, db):
    cursor = db.cursor()
    categoryInsertArr = []
    for category in root_node.findall('shop/categories/category'):
        parentId = 0
        if 'parentId' in category.attrib:
            parentId = category.attrib['parentId']
        id = category.attrib['id']

        text = category.text

        pretyUrl = transliter.transliter(text)

        categoryInsertArr.append((id, parentId, text, pretyUrl))

    print(categoryInsertArr)

    query = """INSERT INTO category(id, parent_id, category, prety_url)
    values(%s, %s, %s, %s)
    """
    cursor.executemany(query,categoryInsertArr)
    db.commit()