def swap16(x):
    return ((x << 8) & 0xFF00) | ((x >> 8) & 0x00FF)


def swap32(x):
    return ((x << 24) & 0xFF000000) | ((x << 8) & 0x00FF0000) | ((x >> 8) & 0x0000FF00) | ((x >> 24) & 0x000000FF)
