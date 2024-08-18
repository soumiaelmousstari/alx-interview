#!/usr/bin/python3


import sys


def ft_print_message(status_code, size_total):

    """"the function of print the message"""
    print("File size: {}".format(size_total))
    for i, j in sorted(status_code.items()):
        if j != 0:
            print("{}: {}".format(i, j))


size_total = 0
a = 0
b = 0
status_code = {"200": 0,
               "301": 0,
               "400": 0,
               "401": 0,
               "403": 0,
               "404": 0,
               "405": 0,
               "500": 0}
try:
    for l in sys.stdin:
        parsed_line = l.split()
        parsed_line = parsed_line[::-1]
        if len(parsed_line) > 2:
            b += 1
            if b <= 10:
                size_total += int(parsed_line[0])
                a = parsed_line[1]
                if (a in status_code.keys()):
                    status_code[a] += 1
            if (b == 10):
                ft_print_message(status_code, size_total)
                b = 0
finally:
    ft_print_message(status_code, size_total)
