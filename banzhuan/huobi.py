import datetime
import logging

import numpy as np

from huobi import HuobiServices
from huobi import Utils
from Bit import api_test
from banzhuan.Bit import xcoin_api_client

api_key = "api_connect_key";
api_secret = "api_secret_key";

api = XCoinAPI(api_key, api_secret);

rgParams = {
	"order_currency" : "BTC",
	"payment_currency" : "KRW"
};
result = api.xcoinApiCall("/public/ticker", rgParams);
huobi_buy=HuobiServices.get_ticker(symbol='btcusdt')['tick']['open']
print(int(result["data"]["buy_price"])*0.0061);
print(huobi_buy)