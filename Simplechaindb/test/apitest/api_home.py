import json
import requests

url='http://10.2.1.22:9984'

r = requests.get(url)
print(r.text)
