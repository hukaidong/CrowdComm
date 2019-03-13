#!/usr/bin/env python
# encoding: utf-8

import unittest
from .numerable import NumerableT, DelegateMethod
from .containable import ContainableT


class Obj(object):
    pass


class TestNum(object, metaclass=NumerableT):
    pass


MAGIC_NUM = 0xC001C0DE
MAGIC_NUM2 = 0xC002C0DE
MAGIC_NUM3 = 0xC003C0DE
VAL = dict(var=MAGIC_NUM)


def vinit():
    '''
    val['var'] == MAGIC_NUM  # Dict
    vcl.var == MAGIC_NUM  # Mimic Attr
    vfn.fn().var == MAGIC_NUM  # Mimic Container
    vcn().fn().var == MAGIC_NUM  # Minmic P-Container
    '''
    global val, vfn, vcl
    val = VAL
    vcl = Obj()
    vcl.__dict__.update(val)
    vfn = Obj()
    setattr(vfn, "fn", lambda : vcl)
    vcn = lambda : vfn


class TestNumMethods(unittest.TestCase):
    def setUp(self):
        vinit()

    def test_dnum(self):
        num = TestNum("var", val, DelegateMethod.BY_IDX)
        self.assertEqual(num, MAGIC_NUM)
        self.assertEqual(1 + num, 1 + MAGIC_NUM)
        self.assertEqual(7 * num, 7 * MAGIC_NUM)
        self.assertEqual(10.0 * num, 10.0 * MAGIC_NUM)
        self.assertEqual(10.0 / num, 10.0 / MAGIC_NUM)

        num.assign(MAGIC_NUM2)
        self.assertEqual(num, MAGIC_NUM2)
        self.assertEqual(val['var'], MAGIC_NUM2)

        val['var'] = MAGIC_NUM3
        self.assertEqual(num, MAGIC_NUM3)

    def test_anum(self):
        num = TestNum("var", vcl, DelegateMethod.BY_ATTR)
        self.assertEqual(num, MAGIC_NUM)
        self.assertEqual(1 + num, 1 + MAGIC_NUM)
        self.assertEqual(7 * num, 7 * MAGIC_NUM)
        self.assertEqual(10.0 * num, 10.0 * MAGIC_NUM)
        self.assertEqual(10.0 / num, 10.0 / MAGIC_NUM)

        num.assign(MAGIC_NUM2)
        self.assertEqual(num, MAGIC_NUM2)
        self.assertEqual(vcl.var, MAGIC_NUM2)

        vcl.var = MAGIC_NUM3
        self.assertEqual(num, MAGIC_NUM3)

    def test_cnum(self):
        num = TestNum("var", vfn.fn, DelegateMethod.BY_CATT)
        self.assertEqual(num, MAGIC_NUM)
        self.assertEqual(1 + num, 1 + MAGIC_NUM)
        self.assertEqual(7 * num, 7 * MAGIC_NUM)
        self.assertEqual(10.0 * num, 10.0 * MAGIC_NUM)
        self.assertEqual(10.0 / num, 10.0 / MAGIC_NUM)

        num.assign(MAGIC_NUM2)
        self.assertEqual(num, MAGIC_NUM2)
        self.assertEqual(vcl.var, MAGIC_NUM2)

        vcl.var = MAGIC_NUM3
        self.assertEqual(num, MAGIC_NUM3)

    def test_call(self):
        num = TestNum("var", lambda : None, DelegateMethod.BY_CALL)
        self.assertRaises(NotImplementedError, lambda :print(num))


class TestContK1(object, metaclass=ContainableT):
    def ChildrenDefs(self):
        self.defattr("var", NumerableK)


class TestContMethod(unittest.TestCase):
    def setUp(self):
        vinit()

    def test_ccnt(self):
        cnt = TestContK1(None, vfn, DelegateMethod.BY_CATT)
        self.assertTrue(hasattr(cnt, 'var'))
        self.assertEqual(cnt.var, MAGIC_NUM)

