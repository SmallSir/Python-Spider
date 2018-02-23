# -*- coding: utf-8 -*-
import random

# Scrapy settings for WangYiMusicTest project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
BOT_NAME = 'WangYiMusicTest'

SPIDER_MODULES = ['WangYiMusicTest.spiders']
NEWSPIDER_MODULE = 'WangYiMusicTest.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'WangYiMusicTest (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'WangYiMusicTest.middlewares.WangyimusictestSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    #'WangYiMusicTest.middlewares.customProxy.RandomProxy':10,
 #   'WangYiMusicTest.middlewares.customUserAgent.RandomUserAgent':30,
  #  'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware':None,
    #'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
MONGO_URI = 'localhost'
MONGO_DB = 'music163'
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'WangYiMusicTest.pipelines.WangyimusictestPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
UserAgents =[
    'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
    'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
    'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
    'Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
    ]
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie':'_ntes_nuid=5e2135ea19041c08d61bddbb9009de63; _ntes_nnid=a387121ca9ed891dca82492f6c088c57,1483420952257; __utma=187553192.690483437.1489583101.1489583101.1489583101.1; __utmz=187553192.1489583101.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __oc_uuid=ff821060-097f-11e7-8c2a-73421a9a1bc4; mail_psc_fingerprint=032ad52396a72877e07f21386dee35a2; NTES_CMT_USER_INFO=106964635%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B06o2qr%7Chttps%3A%2F%2Fsimg.ws.126.net%2Fe%2Fimg5.cache.netease.com%2Ftie%2Fimages%2Fyun%2Fphoto_default_62.png.39x39.100.jpg%7Cfalse%7CbTE1MTUyMzQ3Mjc3QDE2My5jb20%3D; usertrack=c+5+hlkgTIMgjwa+EDUGAg==; _ga=GA1.2.690483437.1489583101; Province=025; City=05278; NTES_PASSPORT=aXWcpL4bYTLQnXY4eO888VlwXt.v922HPG1pBkj.vkeDwsISwc4gjpib7gtylUsoCy.yIGuJPZg7Uq2lTWqIo3A5ddE7eIf5DP_mjdHrg7ky2KFIZHP60ge8g; P_INFO=m15152347277@163.com|1500267468|1|blog|11&10|jis&1499527300&mail163#jis&320800#10#0#0|151277&1|study&blog&photo|15152347277@163.com; UM_distinctid=15d4ee58fc9483-032aae6568b355-333f5902-100200-15d4ee58fca912; NTES_SESS=35juNvuVAClEtPfwjy5rP5GVXVpRFMmwg2ItfudhfLmyGTk4G2l_fIFHi_xsOJTWQrUJvW3JwsMFyepEs0SR6z1_QnKjbQFaesBY9ABy0TVFP_KIiXNgb89wCGe.3_hmKR90f2ybdvNPWqPX8_YesVlIQrWdw5Nfg6KF0EcoVXO3DgV09cJHAeiE_; S_INFO=1500623480|1|0&80##|m15152347277; ANTICSRF=dd45f2a4489d303de869d820a0dadf05; playerid=64643457; JSESSIONID-WYYY=oR0Q0Ce%2Bhldid%2FFtfsiobsg%5Cecyra1qnHBuFFPNBUW%2BbZ3%5C2uq5%2Fqz4VrhRll0%5CaVCfY%2Fg0%2BC47vS%5Cv6rsyuD76tlqWN%2BUryVxph9fZeCmVIDtu5so7vdcdp%2B92hI3A0R5Zm%2Besa5l3ND%5Cz59WOYTY%2FCUjG%2B8gFSGVyzTpMquPQIxyIM%3A1500647790286; _iuqxldmzr_=32; MUSIC_U=f5333454d16d0f0ca5e59b3a82afaabcb107f5e73a4504bae87278f38158d65dbef309e3badc0bfac257abd5a88c5d62dc7e2cf554b1b3fc233a987fb3c42671e386323209b86ec1bf122d59fa1ed6a2; __remember_me=true; __csrf=5cd5b19efc6ea479e298487216162acf; __utma=94650624.776578804.1489210725.1500604214.1500644866.50; __utmb=94650624.28.10.1500644866; __utmc=94650624; __utmz=94650624.1499960824.48.42.utmcsr=yukunweb.com|utmccn=(referral)|utmcmd=referral|utmcct=/412.html',
    'DNT': '1',
    'Host': 'music.163.com',
    'Pragma': 'no-cache',
    'Referer': 'http://music.163.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': random.choice(UserAgents)
}