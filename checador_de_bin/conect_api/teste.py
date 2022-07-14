import requests,json
from urllib import request
a =  555
api = f'https://api-center.000webhostapp.com/api/apistore_binchecker.php?bin={a}'

k = request.urlopen(api)
print(json.loads(k.read()))
