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
    start_urls=['http://m.thepaper.cn/newsDetail_forward_1731732']

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