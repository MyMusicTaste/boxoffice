# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BoxofficeItem(scrapy.Item):
    artist_event = scrapy.Field()
    venue = scrapy.Field()
    rank = scrapy.Field()
    city = scrapy.Field()
    date = scrapy.Field()
    gross_sales = scrapy.Field()
    attend_cap = scrapy.Field()
    shows_sellout = scrapy.Field()
    prices = scrapy.Field()
    promoters = scrapy.Field()
