from PIL import Image
Image.LOAD_TRUNCATED_IMAGES = True
import os
import requests
from io import BytesIO
dir = 'img'

i = 0
def get_img(root_node, db):
    global i
    try:
        os.mkdir(dir)
    except:
        print("Папка img существует")

    for offer in root_node.findall('shop/offers/offer'):
        product_id = offer.attrib['id']
        product_name = offer.find('name').text
        picturesNodes = offer.findall('picture') if offer.findall('picture') else " "
        pictures = list(map(lambda p: p.text, picturesNodes))

        resize_img(pictures, product_id, product_name, db)
        i = i + 1
        print(i)
        # if i == 5:
        #     break

needle_max_side = 800
def resize_img(pictures, product_id, product_name, db):
    n = 0
    for url in pictures:

        ext = url.split('.')[-1]

        tail = "" if n==0 else "_"+str(n)
        filename = transliter(product_name)+tail+"."+ext
        output_url = dir+"/"+ filename

        if os.path.isfile(output_url):
            print('Файл существует ', output_url)
            n = n + 1
            continue

        r = requests.get(url)

        try:
            original_image = Image.open(BytesIO(r.content))
            original_width, original_height = original_image.size
            max_side = original_width if original_width >= original_height else original_height
            size = (original_width, original_height)
        except:
            print('не удалось BytesIO ')
            continue



        if max_side > needle_max_side:
            k = original_width / needle_max_side if original_width >= original_height else original_height / needle_max_side
            needle_width = round(original_width / k)
            needle_height = round(original_height / k)
            size = (needle_width, needle_height)




        try:
            resized_image = original_image.resize(size)
        except:
            print('не удалось ресайзнуть ', original_image)
            continue

        print(product_id, output_url)

        try:
            resized_image.save(output_url)
            n = n + 1
            insertTOSQL(product_id, filename, db)
            if n>2:
                break

        except:
            print('не удалось сохранить ', output_url)
            continue




def insertTOSQL(product_id, src, db):
    cursor = db.cursor()
    imgArr = (product_id, src)
    query = """INSERT INTO img(product_id, src)
    values(%s, %s)
    """
    cursor.execute(query, imgArr)
    db.commit()



def transliter(product_name):
    slovar = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
              'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
              'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
              'ц': 'c', 'ч': 'cz', 'ш': 'sh', 'щ': 'scz', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
              'ю': 'u', 'я': 'ja', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
              'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
              'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
              'Ц': 'C', 'Ч': 'CZ', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'E',
              'Ю': 'U', 'Я': 'YA', ',': '', '?': '', ' ': '_', '~': '', '!': '', '@': '', '#': '',
              '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '-': '', '=': '', '+': '',
              ':': '', ';': '', '<': '', '>': '', '\'': '_', '"': '', '\\': '', '/': '_', '№': '',
              '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
              'Є': 'e', '—': ''}
    for key in slovar:
        product_name = product_name.replace(key, slovar[key])
    return product_name