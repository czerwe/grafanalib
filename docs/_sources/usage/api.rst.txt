api
---



.. code-block:: python

    import grafanalib

    grafanaapi = grafanalib.api('grafanahost.local', port=3000)


Authetification
+++++++++++++++

Via API key (must be created via GUI)

.. code-block:: python

    grafanapi.authKey('kasdfadsfoiasdjfpoaiusdf0977098')


Via basic login with username and password

.. code-block:: python

    grafanapi.authBasic('admin', password='secret')



