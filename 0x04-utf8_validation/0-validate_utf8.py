#!/usr/bin/python3
"""
This script contains a function that checks if a list of integers
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Checks if a list of integers are valid UTF-8 codepoints.

    Parameters:
    data (list): A list of integers representing bytes.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    n = len(data)
    i = 0

    while i < n:
        if data[i] <= 0x7f:
            i += 1
        elif data[i] & 0b11100000 == 0b11000000 and n - i >= 2:
            if data[i+1] & 0b11000000 == 0b10000000:
                i += 2
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000 and n - i >= 3:
            if (
                all(data[j] & 0b11000000 == 0b10000000 for j in range(
                    i+1, i+3
                    ))
            ):
                i += 3
            else:
                return False
        elif data[i] & 0b11111000 == 0b11110000 and n - i >= 4:
            if (
                all(data[j] & 0b11000000 == 0b10000000 for j in range(
                    i+1, i+4
                    ))
            ):
                i += 4
            else:
                return False
        else:
            return False

    return True
