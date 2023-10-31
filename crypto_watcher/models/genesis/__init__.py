from .tokens import create_tokens
from .keepers import create_keepers


def do_genesis():
    create_tokens()
    create_keepers()
