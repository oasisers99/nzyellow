# -*- coding: utf-8 -*-

# Scrapy settings for yellowscrapper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'yellowscrapper'

SPIDER_MODULES = ['yellowscrapper.spiders']
NEWSPIDER_MODULE = 'yellowscrapper.spiders'
#REDIRECT_ENABLED = False
#HANDLE_HTTPSTATUS_LIST = True
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

REDIRECT_ENABLED = False

# DEFAULT_REQUEST_HEADERS = {
# 	#'GET': '/white-all/nail/new-zealand/1/ HTTP/1.1',
# 	#'Host': 'whitepages.co.nz',
# 	#'Connection': 'keep-alive',
# 	'Cache-Control': 'max-age=0',
# 	'Upgrade-Insecure-Requests': '1',
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
# 	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# 	'Referer': 'https://whitepages.co.nz/',
# 	'Accept-Encoding': 'gzip, deflate, sdch, br',
# 	'Accept-Language': 'en-US,en;q=0.8',
# 	'Cookie': 'wpSrc=direct / none; __gads=ID=cd7e6d351d898dae:T=1498701017:S=ALNI_MYQJO0PMxjlUztfD6nUE_Vm0cONNQ; __insp_wid=848114167; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93aGl0ZXBhZ2VzLmNvLm56Lw%3D%3D; __insp_targlpt=V2hpdGUgUGFnZXPCriAtIE5aIEJ1c2luZXNzICYgUmVzaWRlbnRpYWwgRGlyZWN0b3J5; __insp_norec_sess=true; __utmt_yellow=1; __utmt=1; csrftoken=i5B3r7rtJ5RrECmoneO8QR20CCnADAEw; location_info="{\"doubleclick_latest_zone_id\": 3907}"; Oxygenid=kgypvzx2tjob9uukox3ev9c5awkktmq6; searchuuid=3706886e-5c6d-11e7-b0c0-0242c0a8d502; _ga=GA1.3.725816931.1498700983; _gid=GA1.3.463760101.1498700983; __insp_slim=1498706367775; _gat=1; __utma=211115850.725816931.1498700983.1498703792.1498704801.3; __utmb=211115850.30.9.1498706375949; __utmc=211115850; __utmz=211115850.1498704801.3.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)'
# }

# Disable cookies (enabled by default)
#COOKIES_ENABLED = True
#COOKIES_DEBUG = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'yellowscrapper.middlewares.YellowscrapperSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     #'yellowscrapper.middlewares.MyCustomDownloaderMiddleware': 543,
#     'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
#     'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
#     'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 400,
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 500,
#     'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 360, #550,
#     'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
#     'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
#     'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
#     'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
#     'scrapy.downloadermiddlewares.chunked.ChunkedTransferMiddleware': 830,
#     'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
#     'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'yellowscrapper.pipelines.YellowscrapperPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
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
