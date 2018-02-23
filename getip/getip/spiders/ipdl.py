# -*- coding: utf-8 -*-
import scrapy
from getip.items import GetipItem
import time
class IpdlSpider(scrapy.Spider):
    name = 'ipdl'
    start_urls = []
    for i in range(1,20):
        start_urls.append('http://www.xicidaili.com/wt/'+str(i))
    def parse(self, response):
        subSelector = response.xpath('//tr[@class=""]|//tr[@class="odd"]')
        #ii = response.css('.odd')
        items = []
        for sub in subSelector:
            item = GetipItem()
            item['ip'] = sub.css('td::text').extract()[0]
            item['port'] = sub.css('td::text').extract()[1]
            item['protocol'] = sub.css('td::text').extract()[5]
            if(item['protocol'] == 'HTTP'):
                items.append(item)
            #time.sleep()
        return items