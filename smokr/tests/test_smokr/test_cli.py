#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `smokr.cli` module."""
from __future__ import absolute_import

import os

from click.testing import CliRunner

from smokr import cli

dir = os.path.dirname(__file__)
pardir = os.path.abspath(os.path.join(dir, os.path.pardir))


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 2
    assert 'Usage:' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help' in help_result.output
    assert 'Show this message and exit.' in help_result.output
    fail_result = runner.invoke(cli.main,
                                ['-t', os.path.join(pardir,
                                                    'yml',
                                                    'BasicTests.yml'),
                                 '-s', os.path.join(pardir,
                                                    'srcs',
                                                    'test-failure.rb'),
                                 '--fail-fast'])
    assert fail_result.exit_code == 1
    success_result = runner.invoke(cli.main,
                                   ['-t', os.path.join(pardir,
                                                       'yml',
                                                       'BasicTests.yml'),
                                    '-s', os.path.join(pardir,
                                                       'srcs',
                                                       'test.rb')])
    assert success_result.exit_code == 0
