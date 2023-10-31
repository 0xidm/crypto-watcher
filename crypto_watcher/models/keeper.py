from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey, event, Index
from sqlalchemy.orm import backref, relationship

from . import Base, engine
from .utils.crudmixin import CRUDMixin


class Keeper(Base, CRUDMixin):
    __tablename__ = "keeper"
    id = Column(Integer, primary_key = True, nullable=False, autoincrement=True)

    name = Column(String)
    address = Column(String)
    active = Column(Boolean)

    chain_id = Column(Integer, ForeignKey('keeper_chain.id'))
    chain = relationship('KeeperChain', backref=backref('keepers', lazy='dynamic'), foreign_keys=chain_id)

    def __repr__(self):
        return f"Keeper(id={self.id}, name={self.name}, chain={self.chain}, address={self.address})"


class KeeperBalance(Base, CRUDMixin):
    __tablename__ = "keeper_balance"
    id = Column(Integer, primary_key = True, nullable=False, autoincrement=True)

    balance = Column(Float)
    timestamp = Column(DateTime)

    keeper_id = Column(Integer, ForeignKey('keeper.id'))
    keeper = relationship('Keeper', backref=backref('balances', lazy='dynamic'), foreign_keys=keeper_id)

    # Index('keeper_id_idx', keeper_id)

    def __repr__(self):
        return f"KeeperBalance(id={self.id}, keeper={self.keeper.name}, balance={self.balance})"


class KeeperChain(Base, CRUDMixin):
    __tablename__ = "keeper_chain"
    id = Column(Integer, primary_key = True, nullable=False, autoincrement=True)
    name = Column(String)

    def __repr__(self):
        return f"KeeperChain(id={self.id}, name={self.name})"
