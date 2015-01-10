# -*- coding: utf-8 -*-
import os
import tempfile
from nose.tools import ok_, eq_, assert_raises, assert_almost_equals
import oll


class Test_oll(object):

    def __init__(self):
        self.oll = oll.oll('PA1')

    def test__init__(self):
        def _validate_methods(methods):
            for method in methods:
                oll.oll(method)
        methods = ('P', 'AP', 'PA', 'PA1', 'PA2', 'PAK', 'CW', 'AL')
        eq_(None, _validate_methods(methods))

    def test_invalid__init__(self):
        for method_name in ('AWP', 'PY'):
            assert_raises(KeyError, oll.oll, method_name)
        assert_raises(AssertionError, oll.oll, 0)

    def test_add(self):
        for val in (({1.5: 1.0}, 1), ({-1.5: 1.0}, -1)):
            assert_raises(NotImplementedError, self.oll.add, *val)
        for val in (({10: 1.0}, 3), ({10: 1.0}, 0), ({10: 1.0}, -3)):
            assert_raises(ValueError, self.oll.add, *val)

    def test_classify(self):
        self.oll.add({0: 1.0, 1: 2.0, 2: -1.0}, 1)
        self.oll.add({0: -0.5, 1: 1.0, 2: -0.5}, -1)
        assert_almost_equals(self.oll.classify({0: 1.0, 1: 1.0}), 0.171429, 6)

    def test_save_and_load(self):
        try:
            self.oll = oll.oll('PA1')
            self.oll.add({1: 1.0}, 1)
            filename = tempfile.mkstemp()[1]
            self.oll.save(filename)
            ok_(os.path.exists(filename))

            self.oll = oll.oll('PA1')
            self.oll.load(filename)
            assert_almost_equals(self.oll.classify({0: 1.0, 1: 1.0}), 0.5, 6)
        finally:
            os.remove(filename)

    def test_testFile(self):
        try:
            self.oll = oll.oll('PA1')
            self.oll.add({0: 1.0, 1: 1.0}, 1)
            self.oll.add({2: -1.0, 3: -1.0}, -1)
            model_filename = tempfile.mkstemp()[1]
            self.oll.save(model_filename)

            test_filename = tempfile.mkstemp()[1]
            with open(test_filename, 'w') as fd:
                fd.write('+1 0:1.0 1:1.0\n')
                fd.write('-1 2:-1.0 3:-1.0\n')

            actual = self.oll.testFile(test_filename, 0)
            desired = {
                'accuracy': 100.0,
                'true-positive': 1,
                'false-positive': 0,
                'true-negative': 1,
                'false-negative': 0
            }
            eq_(actual, desired)
        finally:
            os.remove(model_filename)
            os.remove(test_filename)

    def test_setC(self):
        self.oll.setC(0.14)

    def test_setBias(self):
        self.oll.setBias(0.14)
