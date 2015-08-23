|Build status| |Documentation Status|

newslynx-sc-shares
==================

Installation
------------

.. code:: bash

    $ mkvirtualenv newslynx-sc-shares
    $ git clone https://github.com/newslynx/newslynx-sc-shares.git
    $ cd newslynx-sc-shares
    $ pip install .

Tests
-----

Requires ``nose``

.. code:: bash

    $ nosetests

Documentation
-------------

Documentation for ``newslynx-sc-shares`` is hosted on `Read The
Docs <http://newslynx-sc-shares.readthedocs.org/>`__.

It's generated via the following steps

-  converts this file (``README.md``) into a ReStructured Text file,
   saving it to
   `docs/index.rst <https://github.com/newslynx/newslynx-sc-shares/blob/master/docs/index.rst>`__
-  runs ``newslynx sc-docs newslynx_sc_shares -f rst`` to generate
   documentation for all the Sous Chefs in ``newslynx-sc-shares`` and
   saves the output to
   `docs/sous-chefs.rst <https://github.com/newslynx/newslynx-sc-shares/blob/master/docs/sous-chefs.rst>`__
-  Builds Sphinx Documentation from these files.

Continuous Integration
----------------------

Builds for ``newslynx-sc-shares`` can be found on
`Travis <https://travis-ci.org/newslynx/newslynx-sc-shares>`__

Contributing
------------

See the `contributing
guidelines <https://github.com/newslynx/newslynx-sc-shares/blob/master/CONTRIBUTING.md>`__.

What's in this module ?
-----------------------

-  `README.md <https://github.com/newslynx/newslynx-sc-shares/blob/master/README.md>`__

   -  This file

-  `VERSION <https://github.com/newslynx/newslynx-sc-shares/blob/master/VERSION>`__

   -  ``newslynx-sc-shares``'s source-of-truth version.

-  `requirements.txt <https://github.com/newslynx/newslynx-sc-shares/blob/master/requirements.txt>`__

   -  ``newslynx-sc-shares``'s python dependencies.

-  `MANIFEST.in <https://github.com/newslynx/newslynx-sc-shares/blob/master/MANIFEST.in>`__

   -  Specifications for which files to include in the PyPI
      distribution.
   -  See the docs on this
      `here <https://docs.python.org/2/distutils/sourcedist.html#specifying-the-files-to-distribute>`__.

-  `setup.py <https://github.com/newslynx/newslynx-sc-shares/blob/master/setup.py>`__

   -  Specification's for building ``newslynx-sc-shares``'s PyPI
      distribution.

-  `.travis.yml <https://github.com/newslynx/newslynx-sc-shares/blob/master/.travis.yml>`__

   -  Configurations for Travis Continuous Integration
   -  You must activate this project on
      `travis-ci.org <https://github.com/newslynx/newslynx-sc-shares/blob/master/http://travis-ci.org/>`__
      for this to run on subsequent updates.

-  `Makefile <https://github.com/newslynx/newslynx-sc-shares/blob/master/Makefile>`__

   -  Helpers for managing ``newslynx-sc-shares``.
   -  Includes:

      -  ``make clean``:

         -  Cleans out cruft from this directory.

      -  ``make install``:

         -  Installs ``newslynx-sc-shares``. Assumes that you're in a
            virtual environment.

      -  ``make all_tests``:

         -  Runs the tests.

      -  ``make readme``

         -  Converts this file to ``.rst``, including a table of
            contents, and saves it to
            `docs/index.rst <https://github.com/newslynx/newslynx-sc-shares/blob/master/docs/index.rst>`__

      -  ``make sous_chef_docs``

         -  Programmtically generates `Sous Chef
            documentation <https://github.com/newslynx/newslynx-sc-shares/blob/master/docs/sous-chefs.rst>`__
            by running
            ``newslynx sc-docs newslynx_sc_shares/ --format=rst > docs/sous-chefs.rst``.

      -  ``make all_docs``:

         -  Builds the sphinx docs for ``newslynx-sc-shares`` by running
            the above two commands.

      -  ``make view_docs``

         -  Serves documentation at
            `localhost:8000 <http://localhost:8000>`__

      -  ``make register``:

         -  Registers ``newslynx-sc-shares`` on
            `PyPI <https://pypi.python.org/pypi>`__.

      -  ``make distribute``:

         -  Publishes a new version of ``newslynx-sc-shares`` to PyPI.

-  `CONTRIBUTING.md <https://github.com/newslynx/newslynx-sc-shares/blob/master/CONTRIBUTING.md>`__

-  `newslynx\_sc\_shares <https://github.com/newslynx/newslynx-sc-shares/blob/master/newslynx_sc_shares/>`__

   -  ``newslynx-sc-shares``'s source code and Sous Chef configuration
      files.

-  `docs <https://github.com/newslynx/newslynx-sc-shares/blob/master/docs/>`__

   -  Sphnix documentation for ``newslynx-sc-shares``

-  `tests <https://github.com/newslynx/newslynx-sc-shares/blob/master/tests/>`__

   -  ``nose`` tests for ``newslynx-sc-shares``

.. |Build status| image:: https://travis-ci.org/newslynx/newslynx-sc-shares.svg
   :target: https://travis-ci.org/newslynx/newslynx-sc-shares
.. |Documentation Status| image:: https://readthedocs.org/projects/newslynx-sc-shares/badge/?version=latest
   :target: https://readthedocs.org/projects/newslynx-sc-shares/?badge=latest

Contents
--------
.. toctree::
	:maxdepth: 2

	index
	sous-chefs
