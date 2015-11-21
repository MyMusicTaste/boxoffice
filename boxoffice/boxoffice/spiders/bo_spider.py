# -*- coding: utf-8 -*-
import scrapy
from ..items import BoxofficeItem

class BOSpider(scrapy.Spider):
    name = "bospider"
    allowed_domains = ["http://www.billboard.com"]
    start_urls = [
        "http://www.billboard.com/biz/current-boxscore/",
    ]

    def parse(self, response):
        table = response.xpath('//table[@class="boxscore_table"]')
        tr = table.xpath('.//tr')[1:]
        for sel in tr:
            row_items = sel.xpath('.//td')
            item = BoxofficeItem()
            item['rank'] = row_items[0].xpath('text()').extract()[0]
            item['artist_event'] = row_items[1].xpath('text()').extract()[0]
            item['venue'] = row_items[2].xpath('text()').extract()[0]
            item['city'] = row_items[3].xpath('text()').extract()[0]
            item['date'] = row_items[4].xpath('text()').extract()[0]
            item['gross_sales'] = row_items[5].xpath('text()').extract()[0]
            item['attend_cap'] = row_items[6].xpath('text()').extract()[0]
            item['shows_sellout'] = row_items[7].xpath('text()').extract()[0]
            item['prices'] = row_items[8].xpath('text()').extract()[0]
            item['promoters'] = row_items[9].xpath('text()').extract()[0]
            yield item
