api
---



.. code-block:: python
    :caption: Core api initialisation
    :name: api init

    import grafanalib

    grafanaapi = grafanalib.api('grafanahost.local', port=3000)


Auth
+++++++++++++++


.. code-block:: python
    :caption: Via API key (must be created via GUI)
    :name: API key login

    grafanapi.authKey('kasdfadsfoiasdjfpoaiusdf0977098')


.. code-block:: python
    :caption: Via basic login with username and password
    :name: Basic Auth login

    grafanapi.authBasic('admin', password='secret')



