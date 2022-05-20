========
Overview
========

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
