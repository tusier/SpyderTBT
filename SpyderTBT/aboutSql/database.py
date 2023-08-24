from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser


class Database:
    def __init__(self):
        config = ConfigParser()
        config.read('scrapy.cfg', encoding='utf-8')
        self.host = config.get('mysql', 'host')
        # self.engine = create_engine('mysql+pymysql://standarduser:zG1ehFbqSPZRWgeU@120.26.10.57:3306/db_zhejiangstd')
        self.engine = create_engine(self.host)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()


db = Database()