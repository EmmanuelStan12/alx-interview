#!/usr/bin/python3
"""UTF-8 Validation
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Validates a list of integers to check
    if they represent a valid UTF-8 encoding.
    Each integer is treated as a byte,
    and the function validates the encoding by
    checking each byte pattern. A UTF-8
    character may consist of 1 to 4 bytes.
    Returns True if data represents a
    valid UTF-8 encoding, else returns False.
    """
    remaining_bytes = 0
    for byte in data:
        if byte > 255 or byte < 0:
            return False
        if remaining_bytes > 0:
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1
        else:
            if (byte >> 7) == 0b0:
                remaining_bytes = 0
            elif (byte >> 5) == 0b110:
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:
                remaining_bytes = 3
            else:
                return False

    return remaining_bytes == 0
