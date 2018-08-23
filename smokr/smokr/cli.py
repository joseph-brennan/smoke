# -*- coding: utf-8 -*-

"""Console script for smokr."""
from __future__ import absolute_import

import sys

import click

from smokr import smokr


@click.command()
@click.option('--config', '-c')
@click.option('--tests', '-t', required=True)
@click.option('--sources', '-s', required=True)
@click.option('--fail-fast/--no-fail-fast', default=False)
def main(tests, sources, fail_fast, config=None):
    """Console test runner for smokr."""
    try:
        smokr.run_tests(tests.split(','), sources.split(','),
                        fail_fast, config)
        return 0
    except AssertionError:
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
