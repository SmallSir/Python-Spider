# -*- coding: utf-8 -*-
import scrapy
import re
import time
import json
from WangYiMusicTest.items import WangyimusictestItem
from WangYiMusicTest.settings import DEFAULT_REQUEST_HEADERS
class MusicspiderSpider(scrapy.Spider):
    base_url = 'https://music.163.com'
    name = 'MusicSpider'
    start_urls = []
    #ids = ['1001', '1002', '1003', '2001', '2002', '2003', '6001', '6002', '6003', '7001', '7002', '7003', '4001',
    #       '4002', '4003']
    ids = ['1001']
    initials = [i for i in range(65, 91)] + [0]
    def start_requests(self):
        for id in self.ids:
            for initial in self.initials:
                url = '{url}/discover/artist/cat?id={id}&initial={initial}'.format(url=self.base_url,id=id,initial=initial)
                yield scrapy.Request(url, dont_filter=True,callback=self.parse)
    #进入排行榜，获取歌手id
    def parse(self, response):
        time.sleep(2)
        base_url = u'http://music.163.com/artist/album?id='
        #/artist/album?id=10998
        names = response.xpath('//*[@id="m-artist-box"]/li/*')
        for i in range(len(names)):
            name_id = names.xpath('//li/p/a[@class="nm nm-icn f-thide s-fc0"]/@href').extract()[i]
            singer = base_url + name_id[12:]
            #print(singer)
            yield scrapy.Request(url=singer,dont_filter=True,callback=self.parse_country)
    #进入歌手界面，搜索歌手专辑页面个数
    def parse_country(self, response):
        time.sleep(2)
        page = response.xpath('//a[@class="zpgi"]/text()').extract()
        page_number = int(page[len(page)-1])
        url = u'http://music.163.com/artist/album?id=3684&limit=12&offset='
        if page_number == None :
            page_number = int(1)
        for i in  range(page_number):
            page_url = url + str(i*12)
            time.sleep(5)
            yield scrapy.Request(url=page_url,callback=self.parse_cds)
    #获取歌手专辑id
    def parse_cds(self,response):
        base_url = u'http://music.163.com'
        cds = response.xpath('//ul[@class="m-cvrlst m-cvrlst-alb4 f-cb"]/li')
        for i in range(len(cds)):
            cd_message = cds.xpath('//li/p[@class="dec dec-1 f-thide2 f-pre"]/a/@href').extract()[i]
            times = cds.xpath('//li/p/span[@class="s-fc3"]/text()').extract()[i]
            messages = base_url + cd_message
            time.sleep(5)
            yield  scrapy.Request(url=messages,dont_filter=True,meta={'times':times},callback=self.parse_cd)
    #进入歌手专辑页面，获取歌曲id
    def parse_cd(self,response):
        base_url = u'http://music.163.com'
        times = response.meta['times']
        songs = response.xpath('//ul[@class="f-hide"]/li')
        for i in range(len(songs)):
            song_id = songs.xpath('//li/a/@href').extract()[i]
            id = song_id[9:]
            song_url = base_url + song_id
            yield scrapy.Request(url=song_url,dont_filter=True,meta={'id':id,'times':times},callback=self.parse_song)
    #进入歌曲界面,获取歌曲信息
    def parse_song(self,response):
        id = response.meta['id']
        base_url = u'http://music.163.com'
        data = {
            'csrf_token': '',
            'params': 'Ak2s0LoP1GRJYqE3XxJUZVYK9uPEXSTttmAS+8uVLnYRoUt/Xgqdrt/13nr6OYhi75QSTlQ9FcZaWElIwE+oz9qXAu87t2DHj6Auu+2yBJDr+arG+irBbjIvKJGfjgBac+kSm2ePwf4rfuHSKVgQu1cYMdqFVnB+ojBsWopHcexbvLylDIMPulPljAWK6MR8',
            'encSecKey': '8c85d1b6f53bfebaf5258d171f3526c06980cbcaf490d759eac82145ee27198297c152dd95e7ea0f08cfb7281588cdab305946e01b9d84f0b49700f9c2eb6eeced8624b16ce378bccd24341b1b5ad3d84ebd707dbbd18a4f01c2a007cd47de32f28ca395c9715afa134ed9ee321caa7f28ec82b94307d75144f6b5b134a9ce1a'
        }
        DEFAULT_REQUEST_HEADERS['Referer'] = base_url + '/playlist?id=' + str(id)
        music_comment = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(id)
        music = response.xpath('//em[@class="f-ff2"]/text()').extract()[0]
        singer = response.xpath('//p[@class="des s-fc4"]//a[@class="s-fc7"]/text()').extract()[0]
        cd = response.xpath('//p[@class="des s-fc4"]//a[@class="s-fc7"]/text()').extract()[-1]
        times = response.meta['times']
        time.sleep(2)
        yield scrapy.FormRequest(music_comment,dont_filter=True, meta={'music':music,'singer':singer,'cd':cd,'times':times},callback=self.parse_comment, formdata=data)
    #获取评论数
    def parse_comment(self,response):
        result = json.loads(response.text)
        item = WangyimusictestItem()
        if(int(result['total']) >= 100000):
            item['cd'] = response.meta['cd']
            item['music'] = response.meta['music']
            item['singer'] = response.meta['singer']
            item['comments'] = result['total']
            item['times'] = response.meta['times']
        return item
