# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

class BoxofficePipeline(object):

    # print("----------------------------------------------------------------------------------------------------")
    def process_item(self, item, spider):

        db = MySQLdb.connect('localhost', 'kokonak', '1234', 'testdatabase')
        cursor = db.cursor()

        query = "CREATE TABLE IF NOT EXISTS testTable(artist_event VARCHAR (255), venue VARCHAR (255));"
        cursor.execute(query)

        artist = item["artist_event"]
        venue = item["venue"]


# artist_event = scrapy.Field()
#     venue = scrapy.Field()
#     rank = scrapy.Field()
#     city = scrapy.Field()
#     date = scrapy.Field()
#     gross_sales = scrapy.Field()
#     attend_cap = scrapy.Field()
#     shows_sellout = scrapy.Field()
#     prices = scrapy.Field()
#     promoters = scrapy.Field()

        # insert into table values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        # args = (item["artist_event"], item["venue"], item["rank"], item["city"], item["date"],
        #         item["gross_sales"], item["attend_cap"], item["shows_sellout"], item["prices"]. item["promoters"])

        query = "insert into testTable values(%s, %s);"
        args = (artist, venue)
        cursor.execute(query, args)

        db.commit()
        db.close()

        return item

    def