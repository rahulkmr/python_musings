#!/usr/bin/env python
import timeit

limit = 10 ** 999


def fib(a=0, b=1, i=1):
    while True:
        if b < limit:
            a, b, i = b, a + b, i + 1
        else:
            return i


print timeit.timeit('fib()', setup='from __main__ import fib', number=20)
