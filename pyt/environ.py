# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division, print_function, absolute_import
import os
import sys
import logging
from collections import Counter


from .compat import *


class TestEnviron(object):
    """This is the Test environment, it manages what the actual test environment
    will look like in certain respects and works as a bridge between the passed in
    cli arguments and settings on the TestCases
    """
    _instance = None
    """singleton"""

    def __init__(self, **kwargs):
        #self.buffer = kwargs.pop("buffer", False)
        #self.debug = kwargs.pop("debug", False)
        #self.warnings = kwargs.pop("warnings", False)
        self.counter = Counter()
#         #pout.v(os.getcwd())
#         self.basedir = self.normalize_dir(os.getcwd())

    @classmethod
    def get_instance(cls, **kwargs):
        if kwargs or not cls._instance:
            cls._instance = cls(**kwargs)
        return cls._instance

#     def normalize_dir(self, d):
#         """get rid of things like ~/ and ./ on a directory
# 
#         :param d: string, the directory to normalize
#         :returns: string, d, now with 100% more absolute path
#         """
#         d = os.path.expanduser(d)
#         d = os.path.abspath(d)
#         return d
# 
#     def unbuffer(self):
#         self.buffer = False

    def update_env_for_test(self, test_count):
        # not sure how much I love messing with the environment right here, but this
        # does propagate down to the test cases
        os.environ['PYT_TEST_COUNT'] = str(test_count)
        os.environ['PYT_TEST_METHOD_COUNT'] = str(self.counter["methods"])
        os.environ['PYT_TEST_CLASS_COUNT'] = str(self.counter["classes"])
        os.environ['PYT_TEST_MODULE_COUNT'] = str(self.counter["modules"])


