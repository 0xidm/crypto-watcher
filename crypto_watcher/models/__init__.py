import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# DB_URI must be set via load_dotenv() or environment variable
engine = create_engine(
    os.getenv('DB_URI', ""),
    echo=False,
)

Base = declarative_base()

Session = scoped_session(
    sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
    )
)


from .token import Token
from .metrics import Metrics
from .keeper import Keeper, KeeperBalance, KeeperChain
