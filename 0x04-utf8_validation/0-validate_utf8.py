#!/usr/bin/python3
"""0. UTF-8 Validation"""


def validUTF8(data):
    c = 0
    for b in data:
        d = bin(b).replace('0b', '').rjust(8, '0')[-8:]
        if c == 0:
           if d.startswith('110'):
                c = 1
            if d.startswith('1110'):
                c = 2
            if d.startswith('11110'):
                c = 3
            if d.startswith('10'):
               return False
        else:
            if not d.startswith('10'):
                return False
            c -= 1
    if c != 0:
        return False
    return True
