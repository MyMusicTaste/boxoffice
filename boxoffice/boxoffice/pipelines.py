# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from BoxLocalDatabase import BoxLocalDatabase

class BoxofficePipeline(object):

    def process_item(self, item, spider):
        db = BoxLocalDatabase()
        db.create_tables()
        db.insert_item(item)

        # print item['shows_sellout']

        return item
