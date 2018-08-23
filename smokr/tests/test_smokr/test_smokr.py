#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `smokr.smokr` module."""
from __future__ import absolute_import

import os
import re

from pytest import raises

from smokr import smokr

curr = os.path.dirname(__file__)
pardir = os.path.abspath(os.path.join(curr, os.path.pardir))

exts = ['java', 'rb', 'cc', 'c', 'sh', 'py', 'clj']


def test_run_tests():
    """Test the Base SmokeTest Class."""
    test_path = os.path.join(pardir, 'yml', 'BasicTests.yml')
    srcsdir = os.path.join(pardir, 'srcs')

    srcs = [os.path.join(srcsdir, filename)
            for _, _, files in os.walk(srcsdir)
            for filename in files
            if filename.split('.')[-1] in exts]

    for src in srcs:
        if re.search(r'test-failure\.[^.]*$', src) is not None:
            with raises(AssertionError):
                smokr.run_tests([os.path.abspath(test_path)], [os.path.abspath(src)], fail_fast=True)
        else:
            smokr.run_tests([os.path.abspath(test_path)], [os.path.abspath(src)], fail_fast=True)
