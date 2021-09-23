import requests

url ='https://export.admitad.com/ru/webmaster/websites/1077576/products/export_adv_products/?feed_id=16430&code=be6217e774&user=nvpost&template=55831'
r = requests.get(url)
r.encoding = 'utf-8'


f = open('xml.xml', 'w+', encoding="utf-8")
f.write(r.text)