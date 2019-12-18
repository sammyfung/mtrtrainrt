# -*- coding: utf-8 -*-
import scrapy


class MtrtrainrtItem(scrapy.Item):
    station = scrapy.Field()
    code = scrapy.Field()
    line = scrapy.Field()
    dir = scrapy.Field()
    time = scrapy.Field()
    dest_code = scrapy.Field()
    dest = scrapy.Field()
    platform = scrapy.Field()
    last_update = scrapy.Field()
    is_delay = scrapy.Field()
