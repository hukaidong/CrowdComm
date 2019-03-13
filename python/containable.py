#!/usr/bin/env python
# encoding: utf-8


#!/usr/bin/env python
# encoding: utf-8

__all__ = {"ContainableT", "DelegateMethod"}


class DelegateMethod:
    BY_ATTR = 'byAttribute'
    BY_CALL = 'byMethod'
    BY_CATT = 'byCalledAttr'
    BY_IDX = 'byIndex'


DM = DelegateMethod


class ContainableT(type):
    def __new__(cls, name, bases, d):
        return super(ContainableT, cls).__new__(cls, name,
                                              (ContainableK, ) + bases, d)

    def __init__(cls, name, bases, d):
        def defattr(self, spec, kls):
            setattr(self, spec, kls(spec, self._value, DM.BY_CATT))

        assert hasattr(cls, "ChildrenDefs")
        setattr(cls, "defattr", defattr)

        super(ContainableT, cls).__init__(name, bases, d)

    def __call__(self, *args, **kwargs):
        self.ChildrenDefs()


class ContainableK(object):
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

    def _value(self, newvalue = None):
        if newvalue:
            self._set_value(newvalue)
            return newvalue
        else:
            return self._get_value()


class ContainerExample(object):
    def ChildrenDefs(self):
        self.defattr("cont", ContainableK)
        self.defattr("x", NumerableK)
        self.defattr("y", NumerableK)
