from datetime import datetime
from SpyderTBT.aboutSql.database import db
from ..Models.nqi_wto_info import NqiStdInfo

class wtonotice:
    def __init__(self):
        self.session = db.get_session()

    def closesession(self):
        self.session.close()

    def insertwtonotice(self,item):
        nqiinfodevdal= NqiStdInfo()
        nqiinfodevdal.title = item.get('title', '')
        nqiinfodevdal.release_date = item.get('release_date', '1900-01-01')
        nqiinfodevdal.content = item.get('content', '')
        nqiinfodevdal.plate = item.get('plate', '')
        nqiinfodevdal.source = item.get('source', '')
        nqiinfodevdal.status = item.get('status', '')
        nqiinfodevdal.create_at = 0
        try:

            self.session.add(nqiinfodevdal)
            self.session.commit()
            print('insert success')
        except Exception as e:
            print(e)

            self.session.rollback()
