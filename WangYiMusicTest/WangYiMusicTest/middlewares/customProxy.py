# -*- coding: utf-8 -*-



from WangYiMusicTest.middlewares.resource import PROXIES
import random
class RandomProxy(object):
    def process_request(self,request,spider):
        proxy = random.choice(PROXIES)
        url = 'http://' + proxy
        request.meta['proxy'] = url