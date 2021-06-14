from pymongo import MongoClient
from .settings import BOT_NAME


class Database:
    def __init__(self, spider):
        db_client = MongoClient()
        self.db = db_client[BOT_NAME]
        self.spider = spider

    def get_urls(self):
        request = self.db[self.spider].find({}, {"url": True})
        return [value["url"] for value in request]

    def insert_one(self, item, spider):
        self.db[spider.name].insert_one(item)

    def find(self, key, value):
        return [el for el in self.db[self.spider].find({key: value})]
