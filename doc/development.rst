Development
===========

Tox
---

All testing is automated using tox.

Coding style
------------

This package uses PEP8 to guide the coding style, and in particular
uses the "black" code formatter to format all code.


Type checking
-------------

The public interfaces contain type annotations for mypy
and all production code must be without warnings from mypy. The testsuite
is not verified using mypy.


Testing
-------

The production code (package "objectgraph") should have full
test coverage. Take care to verify that new code is actually tested
and not just accidently covered.

CI
--

This project uses GitHub Actions for CI and includes publishing new
releases to Test and Prod PyPI.


Releasing
---------

* Check the release notes

* Make sure CI says the build is OK

* Tag the release and push to GitHub

* Create a GitHub release

* Check PyPI
