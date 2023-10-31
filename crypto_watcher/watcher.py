import os
import sys
import time
import logging
import datetime

logging.basicConfig(
    format='%(asctime)s %(module)-16s %(levelname)-8s %(message)s',
    handlers=[logging.FileHandler(os.getenv('WATCHER_LOG_FILENAME', ""))],
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)
print(f"logging to {os.getenv('WATCHER_LOG_FILENAME', '')}")

from .ingest.keepers import FtmKeepersIngest, BscKeepersIngest, BaseKeepersIngest
from .models import Session


class CryptoWatcher(object):
    def __init__(self):
        logger.info("Start Watcher")
        self.ingesters = {}
        for ingester in os.getenv("INGESTERS_ENABLED", "").split(","):
            logger.info(f"Loading ingester {ingester}")
            ingest_cls = globals()[ingester]
            self.ingesters[ingester] = ingest_cls()
        logger.info(f"Ingesters loaded: {self.ingesters.keys()}")

    def update(self):
        logger.info("Update start")

        for ingester_name, ingester_obj in self.ingesters.items():
            try:
                with Session():
                    ingester_obj.update()
                    logger.info(f"Update {ingester_name}")
            except Exception as e:
                logger.error(f"{ingester_name}: {e}")

        logger.info("Update end")

    def run(self, timer_delay=60):
        if os.getenv("DEBUG", "").lower() == "true":
            logger.info("Running in debug mode, exiting after one iteration")
            self.update()
            sys.exit(0)

        while True:
            # wait for the top of the minute
            while int(datetime.datetime.now().timestamp()) % timer_delay != 0:
                time.sleep(0.1)

            # do the update
            self.update()

            # sleep one second to prevent extra iterations
            time.sleep(1)
