import json
import requests

def get_ticker():
	
	url = 'http://www.coolcoin.com/api/v1/ticker'
	res=requests.get(url,data={'coin':'eth'})
	print(res.json())
	
def Trade_add():
	url = 'http://www.coolcoin.com/api/v1/trade_add'
	data = {
		'key'}
	res = requests.post(url)
	
get_ticker()