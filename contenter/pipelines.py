# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from contenter.db_api import Database


class ContenterPipeline:
    def process_item(self, item, spider):
        return item


class MongoPipeline:
    def process_item(self, item, spider):
        db = Database(spider)
        db.insert_one(item, spider)
        return item
