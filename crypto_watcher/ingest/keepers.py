import os
import json
import logging
import datetime

from web3 import Web3, HTTPProvider
from web3.middleware import simple_cache_middleware, geth_poa_middleware

from ..models import Keeper, KeeperBalance, KeeperChain
from . import Ingest

logger = logging.getLogger("crypto-watcher")


class KeepersIngest(Ingest):
    def __init__(self):
        # find all keepers for this chain
        self.keepers = Keeper.query().filter(Keeper.chain_id == self.chain_id, Keeper.active == True).all()
        logger.info(f"Start with {self.keepers}")

    ###
    # Update

    def update(self):
        counter = 0
        
        block_timestamp = self.w3.eth.getBlock("latest").timestamp
        timestamp = datetime.datetime.fromtimestamp(block_timestamp).astimezone(datetime.timezone.utc)

        for keeper in self.keepers:
            g = KeeperBalance.create(
                keeper=keeper,
                balance=self.w3.eth.get_balance(keeper.address) / 10**18,
                timestamp=timestamp,
            )
            if g:
                counter += 1

        logger.info(f"Keepers collected {counter} results")
        return True

class FtmKeepersIngest(KeepersIngest):
    def __init__(self):
        self.w3 = Web3(HTTPProvider(os.getenv("WEB3_PROVIDER_URI", "")))
        self.w3.middleware_onion.add(simple_cache_middleware)
        self.gas_token_name = "FTM"

        self.chain = KeeperChain.find(name="ftm")
        self.chain_id = self.chain.id

        # as final step, call super
        super().__init__()


class BscKeepersIngest(KeepersIngest):
    def __init__(self):
        self.w3 = Web3(HTTPProvider(os.getenv("BSC_WEB3_PROVIDER_URI", "")))
        self.w3.middleware_onion.add(simple_cache_middleware)
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.gas_token_name = "BNB"

        self.chain = KeeperChain.find(name="bsc")
        self.chain_id = self.chain.id

        # as final step, call super
        super().__init__()


class BaseKeepersIngest(KeepersIngest):
    def __init__(self):
        self.w3 = Web3(HTTPProvider(os.getenv("BASE_WEB3_PROVIDER_URI", "")))
        self.w3.middleware_onion.add(simple_cache_middleware)
        # self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.gas_token_name = "ETH"

        self.chain = KeeperChain.find(name="base")
        self.chain_id = self.chain.id

        # as final step, call super
        super().__init__()
