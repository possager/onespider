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
    urls=['http://news.xinhuanet.com/renshi/2017-07/15/c_1121323532.htm']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url,headers={
                'Upgrade-Insecure-Requests':1,
                'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
            })

    def parse(self, response):
        thisdict,thisclass=deal_response.deal_response(response)
        xpath=get_content.getxpath(thisdict)
        title_return=get_title.get_title(thisclass)
        print xpath[0]
        print title_return#title是一个只包含一个内容的的字典http://www.toutiao.com/a6442531519646368002/{title:xpath}
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