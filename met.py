import datetime
import logging

import numpy as np

from huobi import HuobiServices
from huobi import Utils
import pprint

import sys


huobi_high=int(HuobiServices.get_ticker(symbol='btcusdt')['tick']['high']
huobi_low=int(HuobiServices.get_ticker(symbol='btcusdt')['tick']['low']
while True:
	huobi_buy=int(HuobiServices.get_ticker(symbol='btcusdt')['tick']['bid'])
	if huobi_buy==huobi_high-huobi_low:
		HuobiServices.buyMarket(amount,None,'btc','buy-market')
		if 'ok' not in res or res['status'] != 'ok':
			print('购买失败')
			return None
			order_id = res['data']
			order_info = self.HuobiServices.order_info(order_id)
			print(order_info)
				

