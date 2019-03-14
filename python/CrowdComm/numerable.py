#!/usr/bin/env python
# encoding: utf-8

__all__ = {"NumerableT"}

from .baseball import BaseBallK

class NumerableT(type):
    def __new__(cls, name, bases, d):
        return super(NumerableT, cls).__new__(cls, name,
                                              (NumerableK, ) + bases, d)

    def __init__(cls, name, bases, d):
        dtype = getattr(cls, "dtype", float)

        def call_on_value(op):
            def warp(self, *args, **kargs):
                return getattr(dtype(self._get_value()), op).__call__(
                    *args, **kargs)

            return warp

        def delegator(self, name):
            return getattr(self._get_value(), name)

        assert hasattr(cls, "DELE_OPS")
        for op in cls.DELE_OPS:
            setattr(cls, op, call_on_value(op))

        setattr(cls, "__getattr__", delegator)

        super(NumerableT, cls).__init__(name, bases, d)


class NumerableK(BaseBallK):
    DELE_OPS = [
        "__eq__", "__gt__", "__lt__", "__ge__", "__lt__", "__le__", "__add__",
        "__mod__", "__mul__", "__truediv__", "__floordiv__", "__neg__",
        "__pow__", "__radd__", "__rsub__", "__rmul__", "__repr__",
        "__rtruediv__", "__rfloordiv__"
    ]

    def assign(self, value):
        self._set_value(value)
