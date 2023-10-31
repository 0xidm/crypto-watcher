from ..token import Token

def create_tokens():
    for token in tokens:
        t = Token.find_or_create(**token)
        print(f"Created {t}")


tokens = [
    {
        "symbol": 'MPX',
        "name": "Morphex",
        "coingecko_id": "mpx",
        'ftm_address': "0x66eed5ff1701e6ed8470dc391f05e27b1d0657eb"
    },
]
