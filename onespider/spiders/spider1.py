#_*_coding:utf-8_*_
import scrapy
from onespider import deal_response
from onespider import get_content
from onespider import get_title
from onespider import get_content_block
from onespider import get_image
from onespider import get_publish_time

class apider_finally_test(scrapy.Spider):
    name = 'spider_one'
    #http://m.taihainet.com/news/xmnews/shms/2006-04-09/281.html没抓到内容,因为空格太多
    #http://m.taihainet.com/news/twnews/twdnsz/2006-04-05/173.html#没定位到主要的界面模块
    #http://m.taihainet.com/news/twnews/twdnsz/2006-03-28/45.html改了之后还是没有抓到正文内容
    #添加tl过滤功能后还有问题http://m.taihainet.com/news/txnews/gjnews/sh/2006-11-05/191.html
    start_urls=['http://m.taihainet.com/news/txnews/gjnews/sh/2006-11-05/191.html']

    def parse(self, response):
        thisdict,thisclass=deal_response.deal_response(response)
        xpath=get_content.getxpath(thisdict)
        title_return=get_title.get_title(thisclass)
        print xpath[0]
        print title_return#title是一个只包含一个内容的的字典{title:xpath}
        title= title_return.keys()[0]
        title_xpath= title_return.values()[0]
        print title
        print title_xpath

        for i in response.xpath(xpath[0]):
            for jj in i.xpath('text()').extract():
                print jj
        content_block_xpath = get_content_block.get_content_block(xpath_content=xpath[0],xpath_title=title_xpath)
        content_block=response.xpath(content_block_xpath).extract()[0]
        image_list=get_image.get_image(content_block)
        print image_list
        print get_publish_time.find_time(content_block)
