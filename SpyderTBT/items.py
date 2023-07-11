# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class responseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    areaName = scrapy.Field()
    spsid = scrapy.Field()
    tbdate = scrapy.Field()
    tbtitle = scrapy.Field()
    tbtno = scrapy.Field()
    tbtype = scrapy.Field()


class TBTNotificationItem(scrapy.Item):
    tbh = scrapy.Field()
    fwrq = scrapy.Field()
    xbt = scrapy.Field()
    tbcy = scrapy.Field()
    tbbt = scrapy.Field()
    ygsnr = scrapy.Field()
    fzjg = scrapy.Field()
    fgcp = scrapy.Field()
    syyy = scrapy.Field()
    ys = scrapy.Field()
    ywlj = scrapy.Field()
    nrjs = scrapy.Field()
    mdly = scrapy.Field()
    ktgxgwj = scrapy.Field()
    npzrq = scrapy.Field()
    nsxrq = scrapy.Field()
    wbkcyxjgdd = scrapy.Field()
    tbyjtk = scrapy.Field()
    tbyjtkqt = scrapy.Field()
    ICS = scrapy.Field()
    HS = scrapy.Field()
    bk = scrapy.Field()
    PageUrl = scrapy.Field()
    status = scrapy.Field()
    insert_time = scrapy.Field()
    xbt_b = scrapy.Field()
