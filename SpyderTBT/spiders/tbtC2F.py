from configparser import ConfigParser

import scrapy
from redis import Redis

from ..items import TBTNotificationItem
from ..sometools.obtainurls import ObtainUrls

config = ConfigParser()
config.read('scrapy.cfg')
redis_host = config.get('redis', 'host')
redis_port = int(config.get('redis', 'port'))
redis_password = config.get('redis', 'password')
redis_db = int(config.get('redis', 'db'))
class Tbtc2fSpider(scrapy.Spider):
    name = "tbtC2F"
    allowed_domains = ["www.tbt-sps.gov.cn"]
    start_urls = ["http://www.tbt-sps.gov.cn/"]

    def __init__(self, name=None, **kwargs):
        self.red = Redis(host=redis_host, port=redis_port, password=redis_password, db=redis_db)
        super(Tbtc2fSpider, self).__init__(name, **kwargs)
        self.headers = {'Host': 'www.tbt-sps.gov.cn',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                        }

    def start_requests(self):
        obtain=ObtainUrls()
        tbtlist=obtain.requestTBTC2F()
        for i in range(0,len(tbtlist)):
            areaName = tbtlist[i]["areaName"]
            spsid = tbtlist[i]["spsid"]
            tbdate = tbtlist[i]["tbdate"]
            tbtitle = tbtlist[i]["tbtitle"]
            tbtno = tbtlist[i]["tbtno"]
            tbtype = tbtlist[i]["tbtype"]
            completeurl = "http://www.tbt-sps.gov.cn/tbt/" + tbtype + "/" + spsid
            yield scrapy.Request(url=completeurl, headers=self.headers, callback=self.parse)

    def parse(self, response, **kwargs):
        result = self.red.sismember('tbt:tbtC2F_Url', response.url) # 这里是去重，虽然scrapy天然去重，但姑且做一下
        if result:
            print("已经爬过了")
        else:
            spsid = response.url.split("/")[-1]
            obtain = ObtainUrls()
            tbtlist = obtain.obtaintbtData(spsid)
            print("这里是tbtlist!!!!!!!!!!!!!")
            print(tbtlist)

            # print(sel)
            # 这里解析内容页面
            notificate = TBTNotificationItem()
            # print("进入内容!!!")
            notificate['tbh'] = tbtlist.get('tbtno', '')  # 这里是通报号
            notificate['fwrq'] = tbtlist.get('tbdate', '1900-01-01')  # 这里是发文日期
            notificate['xbt'] = '以下通报根据TBT协定第10.6条分发'  # 这里是补遗备注
            notificate['tbcy'] = tbtlist.get('areaName', '')  # 这里是通报成员
            notificate['tbbt'] = tbtlist.get('tbtitle', '')  # 这里是通报标题
            notificate['ygsnr'] = tbtlist.get('tbcontent', '')  # 这里是带格式内容
            notificate['fzjg'] = tbtlist.get('responsibleorganization', '')  # 这里是负责机构
            notificate['fgcp'] = tbtlist.get('productscovered', '')  # 这里是覆盖产品
            notificate['syyy'] = tbtlist.get('tblanguage', '')  # 这里是使用语言
            notificate['ys'] = tbtlist.get('tbpage', '')  # 这里是页数
            notificate['ywlj'] = tbtlist.get('linkurl', '')  # 这里是原文链接
            notificate['nrjs'] = tbtlist.get('tbcontent', '')  # 这里是内容介绍
            notificate['mdly'] = tbtlist.get('purposereason', '')  # 这里是目的理由
            notificate['ktgxgwj'] = tbtlist.get('relevantfile', '')  # 这里是相关文件
            notificate['npzrq'] = tbtlist.get('napprdate', '1900-01-01')  # 这里是拟批准日期
            notificate['nsxrq'] = tbtlist.get('neffedate', '1900-01-01')  # 这里是拟生效日期
            notificate['wbkcyxjgdd'] = tbtlist.get('sourcelink', '')  # 这里是外部可查阅性及规定的地点
            notificate['tbyjtk'] = tbtlist.get('accordingterms', '')  # 这里是通报依据条款
            notificate['tbyjtkqt'] = tbtlist.get('accordingtermsother', '')  # 这里是通报依据条款其他
            notificate['ICS'] = tbtlist.get('icscode', '')  # 这里是ICS
            notificate['HS'] = tbtlist.get('hscode', '')  # 这里是HS
            notificate['bk'] = 'TBT通报'
            notificate['PageUrl'] = response.url
            notificate['status'] = '1'
            notificate['insert_time'] = ''
            notificate['xbt_b'] = ''
            self.red.sadd('tbt:tbtC2F_Url', response.url)
            yield notificate
