# -*- coding: utf-8 -*-



from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from WangYiMusicTest.middlewares.resource import UserAgents
import random


class RandomUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = random.choice(UserAgents)
        request.headers.setdefault('User-Agent',ua)