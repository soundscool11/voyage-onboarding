import requests

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

rows = rjson['RealtimeCityAir']['row']

for row in rows:
    province = row['MSRSTE_NM']
    status = row['IDEX_MVL']
    print(province, status)

