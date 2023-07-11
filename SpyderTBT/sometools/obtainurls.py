# 写一个基础爬虫 目标网站是http://www.tbt-sps.gov.cn/news
# 这个网站有强大的反爬策略 所以每一个请求前面都需要进行一次get请求http://www.tbt-sps.gov.cn/login/getSession?v=
# v的值为当前的13位timestamp值
# 先要对 http://www.tbt-sps.gov.cn/news/find 发送post请求
# 这是json的内容{"title":"","startPublishDate":"","endPublishDate":"","page":1,"type":1,"rows":20}
# 下面开始生成代码
import json
import time
from datetime import datetime

import requests

from .jsreverse import AESCipher
from ..items import responseItem


class ObtainUrls:
    def __init__(self):
        self.now = datetime.now()
        self.response = None
        self.urls = []
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

    def obtaintbtData(self, tbtid):
        url = 'http://www.tbt-sps.gov.cn/tbt/' + str(tbtid)
        response = requests.post(url=url, headers=self.headers)
        print(response.text)
        data = json.loads(response.text)['data']
        aesdecode = AESCipher()
        return aesdecode.decrypt_data(data)

    def requestTBT(self):
        # 一共1459页 ，每页20条 在data里循环，每次data里的page+1
        listresitem = []
        url = 'http://www.tbt-sps.gov.cn/tbt/find'
        for i in range(1, 5):  # 暂时爬这几页
            data = {"keyword": "", "productsCovered": "", "members": "", "hsCode": "", "purposeReason": "",
                    "affectedcorrQt": "", "responsibleorganization": "", "icsCode": "", "startTbdate": "",
                    "endTbdate": "", "page": i, "type": 1, "rows": 20}
            requests.post('http://www.tbt-sps.gov.cn/visit/78')
            response = requests.post(url=url, headers=self.headers, json=data)
            responsejson = json.loads(response.text)
            responsejson = responsejson['data']['data']

            for item in responsejson:
                resitem = responseItem()

                resitem['areaName'] = item['areaName']
                resitem['spsid'] = item['spsid'] if 'spsid' in item else item['tbtid']
                resitem['tbdate'] = item['tbdate']
                resitem['tbtitle'] = item['tbtitle']
                resitem['tbtno'] = item['tbtno']
                resitem['tbtype'] = item['tbtype']

                listresitem.append(resitem)
            time.sleep(2)
        return listresitem

    def requestTBTC2F(self):  # china to foreign
        listresitems = []
        url = 'http://www.tbt-sps.gov.cn/tbt/find'
        for i in range(1, 5):  # 暂时爬这几页
            data = {"keyword": "", "productsCovered": "", "members": "", "hsCode": "", "purposeReason": "",
                    "affectedcorrQt": "", "responsibleorganization": "", "icsCode": "", "startTbdate": "",
                    "endTbdate": "", "page": i, "type": "2", "rows": 20}
            requests.post('http://www.tbt-sps.gov.cn/visit/79')
            response = requests.post(url=url, headers=self.headers, json=data)
            responsejson = json.loads(response.text)
            responsejson = responsejson['data']['data']

            for item in responsejson:
                resitem = responseItem()

                resitem['areaName'] = item['areaName']
                resitem['spsid'] = item['spsid'] if 'spsid' in item else item['tbtid']
                resitem['tbdate'] = item['tbdate']
                resitem['tbtitle'] = item['tbtitle']
                resitem['tbtno'] = item['tbtno']
                resitem['tbtype'] = item['tbtype']

                listresitems.append(resitem)
            time.sleep(2)
        return listresitems
