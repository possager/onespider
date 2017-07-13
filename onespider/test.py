#_*_coding:utf-8_*_
# import requests
# from bs4 import BeautifulSoup
# from lxml import etree
# from onespider import get_image
#
#
# session1=requests.session()
# response=session1.request(method='get',url='http://finance.ifeng.com/a/20170712/15526107_0.shtml')#'/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]'
# # print response.text
#
# datasoup=BeautifulSoup(response.text,'lxml')
# # html_str= datasoup.prettify()
# # selector=etree.HTML(response.text)
# # dataxpath=selector.xpath('/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]')
# # for i in dataxpath:
# #     print i.text
#
# data_result= datasoup.select('html > body > div:nth-of-type(3) > div > div > div')
# # for one in data_result:
# #     print one
#
# print data_result[0]
# print type(data_result[0])
# img_list=get_image.get_image(str(data_result[0]))
# print img_list



import chardet

print chardet.detect('\xa0')