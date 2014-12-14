#!/usr/bin/env python

class thunk(object):
    def __init__(self, fn, *args, **kwargs):
        self.__dict__.update(fn=fn, args=args, kwargs=kwargs)

    def __call__(self):
        return self.fn(*self.args, **self.kwargs)


def trampoline(fn):
    def _trampoline(*args, **kwargs):
        bouncer = fn(*args, **kwargs)
        while isinstance(bouncer, thunk):
            bouncer = bouncer()
        return bouncer
    return _trampoline


@trampoline
def factorial(n):
    def _fact(n, k):
        if n <= 1:
            return k(1)
        else:
            return thunk(_fact, n-1, lambda v: thunk(k, n*v))
    return _fact(n, lambda x: x)

print factorial(1000)

def fact(n, accum=1):
    if n <= 1:
        return accum
    else:
        return thunk(fact, n-1, n*accum)

print trampoline(fact)(1000)
