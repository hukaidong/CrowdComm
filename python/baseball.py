#!/usr/bin/env python
# encoding: utf-8


#!/usr/bin/env python
# encoding: utf-8

__all__ = {'BaseBallK'}

from .universe import DelegateMethod as DM

class BaseBallK(object):

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
