from sqlalchemy import Column, String, Text, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class NqiWtoNotification(Base):
    __tablename__ = 'nqi_wto_notification'

    id = Column(Integer, primary_key=True)
    tbh = Column(String)
    fwrq = Column(DateTime)
    xbt = Column(String)
    tbcy = Column(String)
    tbbt = Column(String)
    ygsnr = Column(Text)  # 修改为Text类型
    fzjg = Column(String)
    fgcp = Column(Text)
    syyy = Column(String)
    ys = Column(String)
    ywlj = Column(String)
    nrjs = Column(Text)
    mdly = Column(Text)
    ktgxgwj = Column(Text)
    npzrq = Column(String)
    nsxrq = Column(String)
    wbkcyxjgdd = Column(Text)
    tbyjtk = Column(String)
    tbyjtkqt = Column(String)
    ICS = Column(String)
    HS = Column(String)
    bk = Column(String)
    PageUrl = Column(String)
    status = Column(String)
    insert_time = Column(String)
    xbt_b = Column(String)
