# -*- coding: utf-8 -*-

"""Main module."""
from __future__ import absolute_import

import re
import shlex
import unittest
from os import path
from subprocess import Popen, PIPE

import yaml

from smokr.runner import SmokeTestRunner

__all__ = ['run_tests']

exts = [
    [
        {
            'cc': 'g++ -g {source} -o {dest}',
            'c': 'gcc -g {source} -o {dest}',
            'java': 'javac {source}',
        },
        ''
    ],
    [
        {
            'sh': 'sh {source}',
            'rb': 'ruby {source}',
            'clj': 'clojure {source}',
            'cc': '{dest}',
            'c': '{dest}',
            'py': 'python {source}',
            'java': lambda source, dest:
                'java -cp {0} {1}'.format(dest[:dest.rindex('/')],
                                          dest[dest.rindex('/') + 1:]),
        },
        'sh {source}'
    ],
    [
        {
            'cc': 'rm -f {dest}',
            'c': 'rm -f {dest}',
            'java': 'rm -f {dest}.class',
        },
        ''
    ]
]


class SmokeTest(unittest.TestCase):
    """Smoke I/O unittest base."""

    def __init__(self, source, name, config=None):
        super(SmokeTest, self).__init__(name)
        self.config = config
        dest = source[:source.rindex('.')]
        ext = source.split('.')[-1]
        actions = [conf.get(ext, default).format(source=source, dest=dest)
                   if isinstance(conf.get(ext, default), str)
                   else conf.get(ext, default)(source, dest)
                   for conf, default in exts]
        self.source = source
        self.setup = shlex.split(actions[0])
        self.runner = shlex.split(actions[1])
        self.teardown = shlex.split(actions[2])

    def run_program(self, input_stream):
        """runs a program from source on the given input."""
        if self.setup:
            Popen(self.setup,
                  stdout=PIPE, stderr=PIPE, stdin=PIPE).communicate()
        try:
            p = Popen(self.runner, stdout=PIPE, stderr=PIPE, stdin=PIPE)
            out, err = p.communicate(input=input_stream.encode())

        finally:
            if self.teardown:
                Popen(self.teardown,
                      stdout=PIPE, stderr=PIPE, stdin=PIPE).communicate()

        return [out.decode(), err.decode()]


def _make_test(test, desc):
    inp = test.get('input', '')
    exp = test.get('output', '')
    name = test.get('name', 'Unknown test')
    err_msg = "{desc}: {src}\n"

    separator = "+" * 80 + "\n"

    def test_method(self, *_args, **_kwargs):
        """Inner test method runner."""
        act, err = self.run_program(inp)
        msg = err_msg
        if err:
            msg += separator + err

        self.assertEqual(exp, act, msg.format(src=self.source, desc=desc))

    test_method.__name__ = name
    test_method.__doc__ = desc
    return test_method


def _make_tests(suite_class, source, filename):
    """Creates a test-set from a yaml configuration."""

    with open(filename) as ymlfile:
        yml = yaml.load(ymlfile.read())
        suite_desc = yml.get('description', 'Unknown Suite')

    tests_set = {}
    for test in yml.get('tests', []):
        test_method = _make_test(test, suite_desc)
        tests_set.update({test_method.__name__: test_method})

    names = list(tests_set.keys())
    test_case = type(suite_class, (SmokeTest,), tests_set)

    suite = unittest.TestSuite()
    suite.addTests(test_case(source, name) for name in names)

    return suite


def run_tests(test_files, sources, fail_fast=False, config=None):
    """Runs tests found in `test_files`."""
    if config:
        config = path.abspath(config)

    runner = SmokeTestRunner(config=config)

    for source in sources:
        print("File:", source)
        print('-' * 79)
        for test_file in test_files:
            filename = path.abspath(test_file)
            suite_path = re.findall(r'/?([^/]*)', test_file)
            suite_class = str(''.join(part.title() for part in suite_path))
            suite = _make_tests(suite_class, source, filename)
            result = runner.run(suite)
            if fail_fast and not result.wasSuccessful():
                raise AssertionError
