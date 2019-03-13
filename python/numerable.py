#!/usr/bin/env python
# encoding: utf-8

__all__ = {"NumerableT", "DelegateMethod"}


class DelegateMethod:
    BY_ATTR = 'byAttribute'
    BY_CALL = 'byMethod'
    BY_CATT = 'byCalledAttr'
    BY_IDX = 'byIndex'


DM = DelegateMethod


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


class NumerableK(object):
    DELE_OPS = [
        "__eq__", "__gt__", "__lt__", "__ge__", "__lt__", "__le__", "__add__",
        "__mod__", "__mul__", "__truediv__", "__floordiv__", "__neg__",
        "__pow__", "__radd__", "__rsub__", "__rmul__", "__repr__",
        "__rtruediv__", "__rfloordiv__"
    ]

    def __init__(self, spec, parent, method, **kargs):
        self._p = parent
        self._v = spec
        self._m = method
        self._k = kargs

    def _get_value(self):
        if self._m == DM.BY_IDX:
            return self._p[self._v]
        elif self._m == DM.BY_CALL:
            raise NotImplementedError()
            # return self._p(self._v)
        elif self._m == DM.BY_ATTR:
            return getattr(self._p, self._v)
        elif self._m == DM.BY_CATT:
            return getattr(self._p(), self._v)

    def _set_value(self, value):
        if self._m == DM.BY_IDX:
            self._p[self._v] = value
        elif self._m == DM.BY_CALL:
            raise NotImplementedError()
            # self._p(self._v, value)
        elif self._m == DM.BY_ATTR:
            setattr(self._p, self._v, value)
        elif self._m == DM.BY_CATT:
            setattr(self._p(), self._v, value)

    def assign(self, value):
        self._set_value(value)
