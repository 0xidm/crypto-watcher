import os
import logging

import click

from dotenv import load_dotenv
load_dotenv()

from crypto_watcher.models.utils.admin import dump_all, load_all, drop_db
from crypto_watcher.models.genesis import do_genesis
from crypto_watcher.models import *

CSV_PATH = os.getenv('CSV_PATH')
logger = logging.getLogger('manager')


@click.group()
def cli():
    pass

@cli.command()
def drop():
    drop_db()

@cli.command()
def genesis():
    do_genesis()

@cli.command()
def repl():
    import IPython
    IPython.embed()

@cli.command()
def dump():
    dump_all(CSV_PATH)

@cli.command()
def load():
    load_all(CSV_PATH)


if __name__ == "__main__":
    cli()
