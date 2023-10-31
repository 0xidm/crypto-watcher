def unpack_network(network):
    if network == "ftm":
        return 250
    elif network == "eth":
        return 1


def unpack_duration(duration):
    if duration == "1h":
        interval = 1
    elif duration in ["24h", "1d"]:
        interval = 24
    elif duration in ["7d", "1w"]:
        interval = 24 * 7
    else:
        interval = 1

    return interval
