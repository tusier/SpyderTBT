import json

import requests
import scrapy

from SpyderTBT.items import TBTNoticeItem


class WtoLawSpider(scrapy.Spider):
    name = "wto_news"
    allowed_domains = ["www.tbtsps.cn"]  # http://www.tbtsps.cn/pc/news#
    start_urls = ["http://www.tbtsps.cn/"]

    def __init__(self, name=None, **kwargs):#伪装浏览器
        self.headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Content-Type': 'application/json',
            'Origin': 'http://www.tbtsps.cn',
            'Referer': 'http://www.tbtsps.cn/pc/news',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', }

    def start_requests(self):
        url = 'http://www.tbtsps.cn/news/find'#目标地址的接口
        for i in range(1, 2):  # 第一次全爬500，之后改成3
            data = {"title": "", "startPublishDate": "", "endPublishDate": "", "page": i, "type": "56", "rows": 20}# 请求参数
            yield scrapy.Request(url=url, method='POST', body=json.dumps(data), headers=self.headers, callback=self.parse)

    def parse(self, response, **kwargs):
        responselist = json.loads(response.text)
        print(responselist)
        for res in responselist['data']['data']:# 遍历数据
            if res.get('isNews')=='1':
                notificate=TBTNoticeItem()
                notificate['title']=res.get('title','') # 标题
                notificate['release_date']=res.get('publishdate','') # 发布时间
                notificate['content']=requests.get('http://www.tbtsps.cn/news/1/'+res.get('keyId',''),headers=self.headers).text # 内容
                notificate['plate'] = '中国技术性贸易措施网' # 板块
                notificate['source']= '标准新闻' # 来源
                notificate['status']=1 # 状态
                notificate['create_at']=0 # 创建时间
                yield notificate
            else:
                continue
