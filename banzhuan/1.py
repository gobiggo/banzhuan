# coding=utf-8
import requests
from lxml import html

url = 'http://www.jinse.com/'
r=requests.get(url).text
tree = html.fromstring(r)
els = tree.xpath('//*[@id="quotation-neirong"]/ul[1]/li/ul/li[2]/span/text()')

el=els[3].strip('￥')
el1=els[2].strip('￥')
huobi=int(el[:3]+el[4:-3])
bit =int(el1[:3]+el1[4:-3])
#print(int(el[:3]+el[4:-3]))
#print(int(els[0].strip('￥，')))
#//*[@id="quotation-neirong"]/ul[1]/li[3]/ul/li[2]/span

