from sqlalchemy import Column, String, Text, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class NqiStdInfo(Base):
    __tablename__ = 'nqi_wto_info'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    release_date = Column(DateTime)
    plate = Column(String)
    source = Column(String)
    status = Column(Integer)
    create_at = Column(Integer)
