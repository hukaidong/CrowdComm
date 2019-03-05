#!/usr/bin/env python
# encoding: utf-8

from functools import partialmethod

class NumberableT(type):
    def __new__(cls, name, bases, d):
        return super(NumberableT, cls).__new__(cls, name, (NumberableK,) + bases, d)

    def __init__(cls, name, bases, d):
        def call_on_value(op):
            def warp(self, *args, **kargs):
                return getattr(self._get_value(), op).__call__(*args, **kargs)
            return warp

        for op in [
                "__eq__", "__gt__", "__lt__", "__ge__", "__lt__", "__le__",
                "__add__", "__mod__", "__mul__", "__neg__", "__pow__",
                "__radd__", "__rsub__", "__repr__"]:
            setattr(cls, op, call_on_value(op))

        def delegator(self, name):
            return getattr(self._get_value(), name)
        setattr(cls, "__getattr__", delegator)

        super(NumberableT, cls).__init__(name, bases, d)


class NumberableK(object):

    def __init__(self):
        self._value = 0

    def _get_value(self):
        self._value += 1;
        return self._value;

    def _set_value(self, value):
        self._value = value

    def assign(self, value):
        self._set_value(value)
