import json

import requests
import scrapy

from ..items import TBTNoticeItem


class WtoNoticeSpider(scrapy.Spider):
    name = "wto_notice"
    allowed_domains = ["www.tbt-sps.gov.cn"]
    start_urls = ["http://www.tbt-sps.gov.cn/"]

    def __init__(self, name=None, **kwargs):
        # self.red = Redis(host=redis_host, port=redis_port, password=redis_password, db=redis_db)
        # super(Tbtc2fSpider, self).__init__(name, **kwargs)
        self.headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Content-Type': 'application/json',
            'Origin': 'http://www.tbt-sps.gov.cn',
            'Referer': 'http://www.tbt-sps.gov.cn/tbtsps/0',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }

    def start_requests(self):
        url = 'http://www.tbt-sps.gov.cn/news/find'
        for i in range(1, 35):
            data = {"title": "", "startPublishDate": "", "endPublishDate": "", "page": i, "type": 1, "rows": 20}
            yield scrapy.Request(url=url, method='POST', headers=self.headers, body=json.dumps(data),
                                 callback=self.parse)

    def parse(self, response, **kwargs):
        responselist = json.loads(response.text)
        print(responselist)
        for res in responselist['data']['data']:
            notificate = TBTNoticeItem()
            notificate['title'] = res.get('title', '')
            notificate['release_date'] = res.get('publishdate', '')
            notificate['content'] = requests.get('http://www.tbt-sps.gov.cn/news/' + res.get('id', ''),
                                                 headers=self.headers).text
            notificate['plate'] = '中国WTO/TBT-SPS国家通报咨询网'
            notificate['source'] = 'WTO官网'
            notificate['status'] = 1
            notificate['create_at'] = 0
            yield notificate
