# -*- coding: utf-8 -*-

"""Result and Runner base classes."""
from __future__ import absolute_import, print_function

import sys
from collections import defaultdict
from unittest import result, TextTestRunner

import yaml

__all__ = ['SmokeTestResult', 'SmokeTestRunner']


OK = 'OK'
FAIL = 'FAIL'
SKIP = 'SKIP'


def _cls_name(test):
    return test.__class__.__name__


class SmokeTestResult(result.TestResult):
    """Base Result Formatter Class."""

    def __init__(self, config=None,
                 hooks=None, stream=None,
                 descriptions=None, verbosity=None):
        super(SmokeTestResult, self).__init__(stream, descriptions, verbosity)
        self.stream = stream
        self.config = config
        self.hooks = hooks if hooks is not None else defaultdict(list)
        self.test_results = defaultdict(list)

    def startTestRun(self):
        """Runs pre-suite hooks and setups up test run."""
        super(SmokeTestResult, self).startTestRun()
        self._run_hooks('pre-run')

    def startTest(self, test):
        """Runs pre-test hooks before each test."""
        super(SmokeTestResult, self).startTest(test)
        self._run_hooks('pre-test', test)

    def stopTestRun(self):
        """Once the suite is complete, runs post-suite hooks."""
        super(SmokeTestResult, self).stopTestRun()
        self._run_hooks('post-run')

    def stopTest(self, test):
        """Runs post-test hooks after eac test."""
        super(SmokeTestResult, self).stopTest(test)
        self._run_hooks('pre-test', test)

    def addFailure(self, test, err):
        super(SmokeTestResult, self).addFailure(test, err)
        self._result(FAIL, _cls_name(test), test, self._description(test))

    def addSuccess(self, test):
        super(SmokeTestResult, self).addSuccess(test)
        self._result(OK, _cls_name(test), test, self._description(test))

    def _description(self, test):
        default = test.shortDescription() or str(test)
        if self.config:
            try:
                return self.config.get('description_format', default).format(
                    method_name=str(test),
                    short_description=test.shortDescription() or '')
            except KeyError:
                print(
                    'Bad description format string: {format}\n'
                    'Replacement options are: {{short_description}} and '
                    '{{method_name}}'.format(
                        format=self.config.get('description_format', default)),
                    file=sys.stderr)
                raise
        return default

    def _result(self, result_type, class_name, test, description):
        name = test._testMethodName
        self.test_results[class_name].append((result_type, name,
                                              description))
        if self.stream:
            result = "{name} ({description}) ... {result_type}"

            if self.config:
                result = self.config.get('result_format', result)

            try:
                print(
                    result.format(result_type=result_type, name=name,
                                  description=description),
                    file=self.stream)
            except KeyError:
                print(
                    'Bad result format string: {format}\n'
                    'Replacement options are: {{name}}, {{description}}, '
                    'and {{result_type}}'.format(format=result),
                    file=sys.stderr)
                raise

    def _run_hooks(self, hook_name, *args):
        for hook in self.hooks.get(hook_name, []):
            hook(*args)


class SmokeTestRunner(TextTestRunner):
    """A test runner that will behave exactly like TextTestRunner and will
    additionally configure the resultclass according to config presented
    """

    def __init__(self, config=None, hooks=None):
        super(SmokeTestRunner, self).__init__(resultclass=SmokeTestResult)
        self.config = None
        self.hooks = hooks
        if config is not None:
            with open(config) as config_file:
                self.config = yaml.load(config_file.read())

    def _makeResult(self):
        result = self.resultclass(config=self.config,
                                  hooks=self.hooks,
                                  stream=self.stream,
                                  descriptions=self.descriptions,
                                  verbosity=self.verbosity)
        return result
