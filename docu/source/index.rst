.. grafanalib documentation master file, created by
   sphinx-quickstart on Fri Jun  2 04:31:31 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to grafanalib's documentation!
======================================

DDA Tools is a libary of DDA related tools. Currently the library contains tools that

* can check the status of the DDA application
* can control the DDA application
* can test the DDA application


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage/createdashboard


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. ddatools documentation master file, created by
   sphinx-quickstart on Thu Feb  9 10:36:34 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. toctree::
   :maxdepth: 2
   :caption: Here a detailed description of the tools:

   usage/checks
   usage/control
   usage/test

How to install it
-----------------

.. code-block:: bash

  yum install postgresql gcc python-devel libpqxx-devel python-pip

In the directory "/opt/dfs-dda-docker/demo" you can find the latest ddatool python wheel. You can install it like following

.. code-block:: bash

    pip install "ddatools-x.x.x-py2-none-any.whl"

Comment:

DDATools is based on following packets

* click>=6.6
* PyYAML==3.12
* GitPython>=2.1.1
* requests>=2.5.2,<2.8
* texttable>=0.8.7
* psycopg2==2.6.2
* docker-py==1.10.3
* elasticsearch>=2.0.0,<3.0.0
* unit-xml>=1.7

Usage
-----
.. code-block:: bash

    dda [OPTIONS] COMMAND [ARGS]...

To get an overview on the OPTIONS, COMMANDS and ARGS execute:

.. code-block:: bash

    dda --help
    dda <COMMAND> --help


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
