# -*- coding: utf-8 -*-
import scrapy
from collectips.items import CollectipsItem

class KuaidailiSpider(scrapy.Spider):
    name = "kuaidaili"
    allowed_domains = ["www.kuaidaili.com"]
    start_urls = [
        'http://www.kuaidaili.com/free/inha/1',
    ]
    # def start_requests(self):
        # resps = []
        # for i in range(1,3):
            # resp = scrapy.Request("http://www.kuaidaili.com/free/inha/%s" % i)
            # resps.append(resp)
        # return resps
        
    def parse(self, response):
        a = response.xpath('//*[@id="list"]/table/tbody').extract()
        b = str(a)
        with open('aa.txt', 'wb') as f:
            f.write(b)