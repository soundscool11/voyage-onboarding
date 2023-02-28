import requests

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

print(rjson)