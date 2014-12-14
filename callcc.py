#!/usr/bin/env python


def callcc(fn):
    def cc(x):
        cc = x
    fn(cc)
    return cc


def temp(cc):
    print "I got here."
    cc("This string was passed to continuation.")
    print "This wasn't called."


def display():
    callcc(temp)

display()
