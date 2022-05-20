========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |github-actions|

.. |github-actions| image:: https://github.com/bankstore-fr/python-blockly-runner/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/bankstore-fr/python-blockly-runner/actions

.. |requires| image:: https://requires.io/github/bankstore-fr/python-blockly-runner/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/bankstore-fr/python-blockly-runner/requirements/?branch=main

.. |version| image:: https://img.shields.io/pypi/v/blockly-runner.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/blockly-runner

.. |wheel| image:: https://img.shields.io/pypi/wheel/blockly-runner.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/blockly-runner

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/blockly-runner.svg
    :alt: Supported versions
    :target: https://pypi.org/project/blockly-runner

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/blockly-runner.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/blockly-runner

.. |commits-since| image:: https://img.shields.io/github/commits-since/bankstore-fr/python-blockly-runner/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/bankstore-fr/python-blockly-runner/compare/v0.0.0...main



.. end-badges

Run blockly workspaces directly, without the need to convert it to Python code.

* Free software: MIT license

Installation
============

::

    pip install blockly-runner

You can also install the in-development version with::

    pip install https://github.com/bankstore-fr/python-blockly-runner/archive/main.zip


Documentation
=============


To use the project:

.. code-block:: python

    # Soon.


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
