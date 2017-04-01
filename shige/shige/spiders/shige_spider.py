# coding=utf-8

import scrapy

class ShigeSpider(scrapy.Spider):
    name = 'shige_spider'

    def __init__(self, *args, **kwargs):
        super(ShigeSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        pass