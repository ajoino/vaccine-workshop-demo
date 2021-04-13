Introduction
============

Hi, thank you for choosing this workshop!
In this workshop, I will demonstrate how to use the ``arrowhead_client`` library to create consumers and producers for HTTP and WebSockets clients.
I will also show how to setup the local clouds both for secure and insecure mode, but the examples will use insecure mode for simplicity.
Without further ado, let's get started!

Setting Up Your Local Cloud
---------------------------

We are going to use the docker images to set up the local cloud.
If you are using Windows you will either have to run the .jar files yourself, or use Docker's windows tool.
How to set up those are beyond the scope of this workshop.

.. warning::
    This workshop assumes you are running Linux, either natively or on a local machine.
    I will not show how to set up a local cloud on Windows, but the Python code should still work on Windows.

To get the docker images, clone the

.. code-block::

    git clone https://github.com/eclipse-arrowhead/core-java-spring.git

.. note::
    The ``core-java-spring`` repository is big and will take time to clone.

Then we move to the ``docker`` directory:

.. code-block::

    cd core-java-spring/docker

Now we follow the instructions from the `core-java-spring <https://github.com/eclipse-arrowhead/core-java-spring/tree/docker-update#quickstart_docker>`_ repository:

 1. Create a docker volume for mysql:
    .. code-block::

        docker volume create --name=mysql

    1. If you get the response that the volume already exists, delete it with:
        .. code-block::

            docker volume rm mysql

        and then create the container again.

 2. Copy the ``initSQL.sh`` script next to the docker compose file:
    .. code-block::

        cp ../scripts/initSQL.sh ./

 3. Run the script we just copied:
    .. code-block::

        ./initSQL.sh

 4. **Hidden extra step**.
    Delete a
