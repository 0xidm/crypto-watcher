
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, event
from sqlalchemy.orm import backref, relationship

from . import Base, engine
from .utils.crudmixin import CRUDMixin


class Metrics(Base, CRUDMixin):
    __tablename__ = "metrics"
    id = Column(Integer, primary_key = True, nullable=False)

    timestamp = Column(DateTime)

    token_id = Column(Integer, ForeignKey('token.id'))
    token = relationship('Token', backref=backref('metrics', lazy='dynamic'), foreign_keys=token_id)

    circulating_supply = Column(Float)
    burned = Column(Float)
    total_supply = Column(Float)
    staked_lp = Column(Float)
    staked_x = Column(Float)
    treasury = Column(Float)

    market_cap_usd = Column(Float)
    volume_24h_usd = Column(Float)
    tvl_usd = Column(Float)

    fdv_1y = Column(Float)
    fdv_2y = Column(Float)
    fdv_5y = Column(Float)
    fdv_10y = Column(Float)

    def __repr__(self):
        return f"Metrics(id={self.id}, timestamp={self.timestamp}, token={self.token}, circulating_supply={self.circulating_supply}, total_supply={self.total_supply}, staked_lp={self.staked_lp}, staked_x={self.staked_x}, tvl_usd={self.tvl_usd}, market_cap_usd={self.market_cap_usd}, fdv_1y={self.fdv_1y}, volume_24h_usd={self.volume_24h_usd})"

    @classmethod
    def get_latest(cls, symbol):
        from .token import Token
        t = Token.find(symbol=symbol)
        latest = cls.query(token=t).order_by(cls.id.desc()).first()
        return latest
