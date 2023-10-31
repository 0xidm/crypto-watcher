from .. import Keeper, KeeperBalance, KeeperChain


def create_base_keepers():
    base_chain = KeeperChain.find_or_create(name="base")

    Keeper.find_or_create(
        name="price-1-base",
        chain=base_chain,
        address="0xA058b1A0bA31590d1E14A1F157f4ff7D41c78077",
        active=True
    )

    Keeper.find_or_create(
        name="liquidator-1-base",
        chain=base_chain,
        address="0xb6254092f30A141bF85b2a7e3B2BcEc65d809Dd0",
        active=True
    )

    Keeper.find_or_create(
        name="order-1-base",
        chain=base_chain,
        address="0xD7a38CbC6d7153e1c37Bab3E010cB73dEc6F4971",
        active=True
    )

    Keeper.find_or_create(
        name="position-1-base",
        chain=base_chain,
        address="0x2cd775ac25a8DBD11C4Db46901C776936699f2EE",
        active=True
    )

    print(base_chain)


def create_ftm_keepers():
    ftm_chain = KeeperChain.find_or_create(name="ftm")

    Keeper.find_or_create(
        name="price-1-ftm",
        chain=ftm_chain,
        address="0xA058b1A0bA31590d1E14A1F157f4ff7D41c78077",
        active=True
    )

    Keeper.find_or_create(
        name="liquidator-1-ftm",
        chain=ftm_chain,
        address="0xb6254092f30A141bF85b2a7e3B2BcEc65d809Dd0",
        active=True
    )

    Keeper.find_or_create(
        name="order-1-ftm",
        chain=ftm_chain,
        address="0xD7a38CbC6d7153e1c37Bab3E010cB73dEc6F4971",
        active=True
    )

    Keeper.find_or_create(
        name="position-1-ftm",
        chain=ftm_chain,
        address="0x2cd775ac25a8DBD11C4Db46901C776936699f2EE",
        active=True
    )        

    print(ftm_chain)

def create_bsc_keepers():
    bsc_chain = KeeperChain.find_or_create(name="bsc")

    Keeper.find_or_create(
        name="price-1-bsc",
        chain=bsc_chain,
        address="0xA058b1A0bA31590d1E14A1F157f4ff7D41c78077",
        active=True
    )

    Keeper.find_or_create(
        name="liquidator-1-bsc",
        chain=bsc_chain,
        address="0xb6254092f30A141bF85b2a7e3B2BcEc65d809Dd0",
        active=True
    )

    Keeper.find_or_create(
        name="order-1-bsc",
        chain=bsc_chain,
        address="0xD7a38CbC6d7153e1c37Bab3E010cB73dEc6F4971",
        active=True
    )

    Keeper.find_or_create(
        name="position-1-bsc",
        chain=bsc_chain,
        address="0x2cd775ac25a8DBD11C4Db46901C776936699f2EE",
        active=True
    )

    print(bsc_chain)


def create_keepers():
    create_base_keepers()
    create_ftm_keepers()
    create_bsc_keepers()
