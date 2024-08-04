''' JavaScript Object Notation '''
import json
from urllib.request import urlopen
import ssl

with open('states.json') as f:
  data = json.load(f)

print(type(data['states'][0]))
#for state in data['states']:
#  del state['area_codes']


#with open('new_states.json', 'w') as f:
#  json.dump(data, f, indent=2)

print(json.dumps({"c": 1.1, "b": 2, "a": 1},sort_keys=True))


print(json.dumps([1.1, 2, 3, {'4': 5, '6': 7}]))

print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
context = ssl._create_unverified_context()
with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json", context=context) as response:
  source = response.read()

print(source)
