"""
Module of Encode & Decode Strings
"""
from math import sqrt, log


def encode(decoded: str) -> str:
    """
    Each encrypted password is unique, its security is based on the length and the difference between each character
    """

    encoded = []
    LONG = len(decoded)
    point = 0
    for i in decoded:
        point += ord(i)

    for i in decoded:
        j = ord(i) + (point % LONG)
        encoded.insert(0, chr(j))

    return ''.join(encoded)


def decode(encoded: str) -> str:
    """
    
    """
    decoded = []
    LONG = len(encoded)
    point = 0
    for i in encoded:
        point += ord(i)

    for i in encoded:
        j = ord(i) - (point % LONG)
        decoded.insert(0, chr(j))

    return ''.join(decoded)