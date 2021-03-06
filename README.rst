========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |github-actions|
    * - pypi
      - | |version| |wheel| |supported-versions| |supported-implementations|

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

.. end-badges

Run `blockly workspaces <https://developers.google.com/blockly/>`__ directly, without the need to convert it to Python code.

* Free software: MIT license


Installation
============

Currently, you must install the in-development version with (we are not on `pypi <https://pypi.org>`__ yet)::

    pip install blockly-runner


Documentation
=============

To use the project:

.. code-block:: python

    from blockly_runner import execute_workspace_merge_all_roots, execute_workspace

    # Result will contain all the variable updated to match their new value.
    # If you have many block roots, you will get a global result.
    result = execute_workspace_merge_all_roots(my_dict_workspace, {"var1": 1, "var2": "Hi"})

    # If you have many block roots, you will get a list of result with as many element as you have roots.
    results = execute_workspace(my_dict_workspace, {"var1": 1, "var2": "Hi"})

We currently support:

* Logic with if, if/else, if/else if, negation, comparison operators, logic operations.
* Basic math: create a number variable, basic math operations (+, -, \*, /, ^).
* Basic text: create a text variable.
* Variable management: set a variable, access a variable, change a number variable by a delta.

The following exceptions can be raised:

* ``UndefinedVariable`` if you try to access a variable before it is defined.
* ``InvalidBlock`` if we encounter an invalid block. It shouldn't happen if you pay attention in the interface ;-)
  And it's there it's easier to spot where this error comes from.

Contributions are welcomed to help us go further.


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


Create a new release
====================

You need `flit <https://flit.pypa.io/en/latest/>`__ to publish the release.

#. Bump version in ``src/blockly_runner/__init__.py``.
#. Update the ``CHANGELOG.rst``.
#. Commit and push.
#. Publish the package with ``flit publish``.
