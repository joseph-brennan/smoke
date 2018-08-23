#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `smokr.runner` module."""
from __future__ import absolute_import

import os

from pytest import raises

from smokr import runner, smokr

cur_dir = os.path.dirname(__file__)
par_dir = os.path.abspath(os.path.join(cur_dir, os.path.pardir))
test_dir = os.path.abspath(os.path.join(par_dir, 'yml'))
test_src = os.path.abspath(os.path.join(par_dir, 'srcs', 'test.rb'))
config_result = os.path.join(test_dir, 'Config_Bad-Result.yml')
config_desc = os.path.join(test_dir, 'Config_Bad-Desc.yml')
test_test = os.path.join(test_dir, 'BasicTests.yml')


def test_smoke_result():
    """Test the CLI."""
    r = runner.SmokeTestResult()
    assert r is not None
    assert r.config is None


def test_smoke_runner():
    with raises(KeyError):
        smokr.run_tests([test_test], [test_src], config=config_desc)

    with raises(KeyError):
        smokr.run_tests([test_test], [test_src], config=config_result)
