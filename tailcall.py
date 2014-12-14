#!/usr/bin/env python


class trampoline(object):
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        ret = self.fn(*args, **kwargs)
        while isinstance(ret, thunk):
            ret = ret()
        return ret


class thunk(object):
    def __init__(self, fn, *args, **kwargs):
        self.__dict__.update(fn=fn, args=args, kwargs=kwargs)

    def __call__(self):
        if isinstance(self.fn, trampoline):
            return self.fn.fn(*self.args, **self.kwargs)
        else:
            return self.fn(*self.args, **self.kwargs)


@trampoline
def fact(n, accum=1):
    if n <= 1:
        return accum
    else:
        return thunk(fact, n-1, n*accum)

print fact(1000)


@trampoline
def is_even(n):
    if n == 0:
        return True
    else:
        return thunk(is_odd, n - 1)


@trampoline
def is_odd(n):
    if n == 0:
        return False
    else:
        return thunk(is_even, n - 1)

print is_even(1000001)


def factorial(num, accum=1):
    while True:
        if num <= 1:
            return accum
        else:
            num, accum = num - 1, accum * num


print factorial(10)
