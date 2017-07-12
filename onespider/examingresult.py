import requests
from bs4 import BeautifulSoup

session1=requests.session()

response_data=session1.request(method='GET',url='http://nc.newssc.org/system/20170712/002223214.html')
# print response_data.text
response_data.encoding='gb2312'

datasoup=BeautifulSoup(response_data.text,'lxml')
for i in datasoup.select(' html > body > div:nth-of-type(5) > div > div:nth-of-type(2) > div:nth-of-type(2) > p'):#'/html[1]/body[1]/div[5]/div[1]/div[2]/div[2]/p' (140619042617192)
    print i.text