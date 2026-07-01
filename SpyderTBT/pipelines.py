# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from .aboutSql.tbtF2Cdal import tbtF2Cdal
from .aboutSql.tbtnotice import wtonotice
from .items import TBTNotificationItem

tbtF2cDto = tbtF2Cdal()
tbtnotice=wtonotice()


class SpydertbtPipeline:

    def process_item(self, item, spider):
        print("this is pipline >=+.=>==>")
        item_type=item.__class__.__name__
        method_name = f"process_{item_type.lower()}"
        handler=getattr(self,method_name,None)
        if handler:
            handler(item)
        return item
    def process_tbtnotificationitem(self, item):
        if tbtF2cDto.checkexist(item):
            tbtF2cDto.inserttbtF2C(item)
            print('-----------------------------------charu==----------------------------->')
            tbtF2cDto.closesession()
        else:
            print("已经在库里了，所以没有插入")


    def process_tbtnoticeitem(self,item):
        tbtnotice.insertwtonotice(item)

