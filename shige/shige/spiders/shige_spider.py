# coding=utf-8

import scrapy

class ShigeSpider(scrapy.Spider):
    name = 'shige_spider'

    allowed_domains = ['www.baidu.com']

    start_urls = [
        'http://www.baidu.com'
    ]

    def __init__(self, *args, **kwargs):
        print '1' * 50
        super(ShigeSpider, self).__init__(*args, **kwargs)
        print '2' * 50