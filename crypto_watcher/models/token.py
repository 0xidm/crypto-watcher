import csv

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, event

from . import Base, Session
from .utils.crudmixin import CRUDMixin


class Token(Base, CRUDMixin):
    __tablename__ = "token"
    id = Column(Integer, primary_key = True, nullable=False)
    name = Column(String)
    symbol = Column(String)

    unit = Column(String)
    type = Column(String)
    sector = Column(String)
    crypto_asset_score = Column(Integer)

    last_updated_coingecko = Column(DateTime)

    coingecko_id = Column(String)
    ftm_address = Column(String)
    # address = Column(String)

