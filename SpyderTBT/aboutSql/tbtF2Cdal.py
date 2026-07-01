from datetime import datetime

from SpyderTBT.aboutSql.database import db
from ..Models.nqi_wto_notification import NqiWtoNotification


class tbtF2Cdal:
    def __init__(self):
        self.session = db.get_session()

    def closesession(self):
        self.session.close()

    def checkexist(self, item):
        result = self.session.query(NqiWtoNotification).filter(NqiWtoNotification.tbh == item.get('tbh', '')).first()

        if result is not None:
            # 处理存在记录的情况
            print(f"存在记录，tbh为 {result.tbh}")
            return False
        else:
            # 处理不存在记录的情况
            print("不存在记录")
            return True

    def inserttbtF2C(self, item):
        nqi_wto_notification = NqiWtoNotification()
        nqi_wto_notification.tbh = item.get('tbh', '')
        nqi_wto_notification.fwrq = item.get('fwrq', '')
        nqi_wto_notification.xbt = item.get('xbt', '')
        nqi_wto_notification.tbcy = item.get('tbcy', '')
        nqi_wto_notification.tbbt = item.get('tbbt', '')
        nqi_wto_notification.ygsnr = item.get('ygsnr', '')
        nqi_wto_notification.fzjg = item.get('fzjg', '')
        nqi_wto_notification.fgcp = item.get('fgcp', '')
        nqi_wto_notification.syyy = item.get('syyy', '')
        nqi_wto_notification.ys = item.get('ys', '')
        nqi_wto_notification.ywlj = item.get('ywlj', '')
        nqi_wto_notification.nrjs = item.get('nrjs', '')
        nqi_wto_notification.mdly = item.get('mdly', '')
        nqi_wto_notification.ktgxgwj = item.get('ktgxgwj', '')
        nqi_wto_notification.npzrq = item.get('npzrq', '')
        nqi_wto_notification.nsxrq = item.get('nsxrq', '')
        nqi_wto_notification.wbkcyxjgdd = item.get('wbkcyxjgdd', '')
        nqi_wto_notification.tbyjtk = item.get('tbyjtk', '')
        nqi_wto_notification.tbyjtkqt = item.get('tbyjtkqt', '')
        nqi_wto_notification.ICS = item.get('ICS', '')
        nqi_wto_notification.HS = item.get('HS', '')
        nqi_wto_notification.bk = item.get('bk', '')
        nqi_wto_notification.PageUrl = item.get('PageUrl', '')
        nqi_wto_notification.status = item.get('status', '')
        nqi_wto_notification.insert_time = datetime.now()
        nqi_wto_notification.xbt_b = item.get('xbt_b', '')
        try:
            self.session.add(nqi_wto_notification)
            self.session.commit()
            print('insert success')
        except Exception as e:
            print(e)
            self.session.rollback()
            raise e
