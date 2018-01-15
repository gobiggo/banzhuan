import datetime
import logging

import numpy as np

from huobi import HuobiServices
from huobi import Utils
import pprint
from Bit import xcoin_api_client
import sys

api_key = "d18a0e81dd3d62b1d33fddf89a0724ef";
api_secret = "220f6c043a1e14b37bfe5b1f7537c623";

api = xcoin_api_client.XCoinAPI(api_key, api_secret);

rgParams = {
	"order_currency" : "BTC",
	"payment_currency" : "KRW"
};
result = api.xcoinApiCall("/public/ticker", rgParams);
huobi_buy=int(HuobiServices.get_ticker(symbol='btcusdt')['tick']['open'])*6.4607
Bit_sell=int(result["data"]["sell_price"])*0.0061);
if(Bit_shell>huobi_buy):
	
	
	
	

class start(object):	
	def huobi_buy(self,amount,exchang="huobi"):
			if exchange == "huobi":
				res = self.HuobiServices.buyMarket(amount,None,'btcusdt','buy-market')
				if 'ok' not in res or res['status'] != 'ok':
					print('购买失败')
					return None
				order_id = res['data']
				order_info = self.HuobiServices.order_info(order_id)
				print(order_info)
				
			else:
				pass

	def Bit_sell(self,amount,exchang='Bit'):
			if exchange == 'Bit':
				res=api.xcoinApiCall("/trade/market_buy", units=amount,currency='BTC');
				if '0000' not in res or res['status'] != '0000':
					print('购买失败')
					return None
				order_id = res['order_id']
				
				
				
		
