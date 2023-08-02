from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://standarduser:zG1ehFbqSPZRWgeU@120.26.10.57:3306/db_zhejiangstd')
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()


db = Database()