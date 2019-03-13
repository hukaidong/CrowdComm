#!/usr/bin/env python
# encoding: utf-8


#!/usr/bin/env python
# encoding: utf-8

__all__ = {"ContainableT"}

from .baseball import BaseBallK
from .universe import DelegateMethod as DM

class NotSet:
    pass

class ContainableT(type):
    def __new__(cls, name, bases, d):
        return super(ContainableT, cls).__new__(cls, name,
                                              (ContainableK, ) + bases, d)

    def __init__(cls, name, bases, d):
        def defattr(self, spec, kls):
            setattr(cls, spec, kls(spec, self._value, DM.BY_CATT))

        assert hasattr(cls, "ChildrenDefs")
        setattr(cls, "defattr", defattr)
        super(ContainableT, cls).__init__(name, bases, d)

    def __call__(cls, *args, **kwargs):
        self = super(ContainableT, cls).__call__(*args, **kwargs)
        self.ChildrenDefs()
        return self


class ContainableK(BaseBallK):
    def _value(self, newvalue = NotSet):
        if newvalue is not NotSet:
            self._set_value(newvalue)
            return newvalue
        else:
            return self._get_value()

