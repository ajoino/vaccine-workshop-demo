Creating Providers
==================

Next, we will create a simple provider.
But before we do that, we will create a certificate for the provider.

Creating Certificates
---------------------

One of the most annoying things with setting up local clouds is managing certificates.
`The Onboarding Controller <https://github.com/eclipse-arrowhead/core-java-spring#onboardingcontroller>`_ will remove most of the labor involved, but it is not dockerized yet so we will do it the old way.
We will use the `self-signed certificate guide <https://github.com/eclipse-arrowhead/core-java-spring/blob/master/documentation/certificates/create_client_certificate.pdf>`_ which uses a GUI tool called KeyStore Explorer.
Or rather, you will use it when you create new certificates, I have already created certificates for a provider and consumer for you.

Creating the Provider
---------------------

Open a Python file and type the following:

.. code-block:: python

    from arrowhead_client.client.implementations import SyncClient

    provider = SyncClient.create(
        system_name='vaccine-provider',
        address='127.0.0.1',
        port=1337,
        keyfile=
    )





