#!/usr/bin/python3
"""0.N queens"""
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

N = int(sys.argv[1])


def position(N, i=0, a=[], b=[], c=[]):
    """find positions"""
    if i < N:
        for j in range(N):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(N, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(N):
    """the solve function"""
    k = []
    i = 0
    for so in position(N, 0):
        for s in so:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(N)
