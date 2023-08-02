# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from .aboutSql.tbtF2Cdal import tbtF2Cdal
from .items import TBTNotificationItem

tbtF2cDto = tbtF2Cdal()


class SpydertbtPipeline:
    def process_item(self, item, spider):
        # if isinstance(item, TBTNotificationItem):
            tbtF2cDto.inserttbtF2C(item)


