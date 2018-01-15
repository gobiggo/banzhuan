import HuobiServices
import json

#data = HuobiServices.get_ticker(symbol
data = HuobiServices.get_symbols()
json_data = json.load(data)
print(json_data)
#print(json_data['ticker']['buy'])