#_*_coding:utf-8_*_
import scrapy
from onespider import deal_response
from onespider import get_result
from onespider import title_get
from onespider import get_content_block


class apider_finally_test(scrapy.Spider):
    name = 'spider_one'
    start_urls=['http://finance.ifeng.com/a/20170712/15526107_0.shtml']

    def parse(self, response):
        thisdict,thisclass=deal_response.deal_response(response)
        xpath=get_result.getxpath(thisdict)
        title_return=title_get.get_title(thisclass)
        print xpath[0]
        print title_return#title是一个只包含一个内容的的字典{title:xpath}
        title= title_return.keys()[0]
        title_xpath= title_return.values()[0]
        print title
        print title_xpath

        for i in response.xpath(xpath[0]):
            for jj in i.xpath('text()').extract():
                print jj
        print get_content_block.get_content_block(xpath_content=xpath[0],xpath_title=title_xpath)