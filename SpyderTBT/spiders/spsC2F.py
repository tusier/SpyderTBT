from configparser import ConfigParser

import scrapy
from redis import Redis

from SpyderTBT.items import TBTNotificationItem
from SpyderTBT.sometools.obtainurls import ObtainUrls

# config = ConfigParser()
# config.read('scrapy.cfg')
# redis_host = config.get('redis', 'host')
# redis_port = int(config.get('redis', 'port'))
# redis_password = config.get('redis', 'password')
# redis_db = int(config.get('redis', 'db'))
class Spsc2fSpider(scrapy.Spider):
    name = "spsC2F"
    allowed_domains = ["www.tbt-sps.gov.cn"]
    start_urls = ["http://www.tbt-sps.gov.cn/"]

    def __init__(self, name=None, **kwargs):
        # self.red = Redis(host=redis_host, port=redis_port, password=redis_password, db=redis_db)
        super(Spsc2fSpider, self).__init__(name, **kwargs)
        self.headers = {'Host': 'www.tbt-sps.gov.cn',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                        }

    def start_requests(self):
        obtain = ObtainUrls()
        spslist = obtain.requestSPSC2F()
        for i in range(0, len(spslist)):
            areaName = spslist[i]["areaName"]
            spsid = spslist[i]["spsid"]
            tbdate = spslist[i]["tbdate"]
            tbtitle = spslist[i]["tbtitle"]
            tbtno = spslist[i]["tbtno"]
            tbtype = spslist[i]["tbtype"]
            completeurl = "http://www.tbt-sps.gov.cn/sps/" + tbtype + "/" + spsid
            yield scrapy.Request(url=completeurl, headers=self.headers, callback=self.parse)

    def parse(self, response, **kwargs):
        # result = self.red.sismember('tbt:spsC2F_Url', response.url)
        # if result:
        #     print("已经爬取过了")
        # else:
            spsid = response.url.split("/")[-1]
            obtain = ObtainUrls()
            spslist = obtain.obtainspsData(spsid)
            print("这里是spslist!!!!!!!!!!!!!")
            print(spslist)

            notificate = TBTNotificationItem()

            notificate['tbh'] = spslist.get('tbtno', '')  # 这里是通报号
            notificate['fwrq'] = spslist.get('tbdate', '1900-01-01')  # 这里是发文日期
            notificate['xbt'] = '以下通报根据TBT协定第10.6条分发'  # 这里是补遗备注
            notificate['tbcy'] = spslist.get('areaName', '')  # 这里是通报成员
            notificate['tbbt'] = spslist.get('tbtitle', '')  # 这里是通报标题
            notificate['ygsnr'] = spslist.get('tbcontent', '')  # 这里是带格式内容
            notificate['fzjg'] = spslist.get('responsibleorganization', '')  # 这里是负责机构
            notificate['fgcp'] = spslist.get('productscovered', '')  # 这里是覆盖产品
            notificate['syyy'] = spslist.get('tblanguage', '')  # 这里是使用语言
            notificate['ys'] = spslist.get('tbpage', '')  # 这里是页数
            notificate['ywlj'] = spslist.get('linkurl', '')  # 这里是原文链接
            notificate['nrjs'] = spslist.get('tbcontent', '')  # 这里是内容介绍
            notificate['mdly'] = spslist.get('purposereason', '')  # 这里是目的理由
            notificate['ktgxgwj'] = spslist.get('relevantfile', '')  # 这里是相关文件
            notificate['npzrq'] = spslist.get('napprdate', '1900-01-01')  # 这里是拟批准日期
            notificate['nsxrq'] = spslist.get('neffedate', '1900-01-01')  # 这里是拟生效日期
            notificate['wbkcyxjgdd'] = spslist.get('sourcelink', '')  # 这里是外部可查阅性及规定的地点
            notificate['tbyjtk'] = spslist.get('accordingterms', '')  # 这里是通报依据条款
            notificate['tbyjtkqt'] = spslist.get('accordingtermsother', '')  # 这里是通报依据条款其他
            notificate['ICS'] = spslist.get('icscode', '')  # 这里是ICS
            notificate['HS'] = spslist.get('hscode', '')  # 这里是HS
            notificate['bk'] = 'SPS通报'
            notificate['PageUrl'] = response.url
            notificate['status'] = '1'
            notificate['insert_time'] = ''
            notificate['xbt_b'] = ''
            # self.red.sadd('tbt:spsC2F_Url', response.url)
            yield notificate
