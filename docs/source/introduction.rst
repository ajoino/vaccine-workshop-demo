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

To get the docker images, clone the `workshop github repository <https://github.com/ajoino/vaccine-workshop-demo>`_.

.. code-block::

    git clone https://github.com/ajoino/vaccine-workshop-demo.git

Then we move to the ``docker`` directory:

.. code-block::

    cd docker

Run the ``initSQL.sh`` script:

.. code-block::

    ./initSQL.sh

Create a ``mysql`` docker volume:

.. code-block::

    docker volume create --name=mysql

Now we should be able to start the docker images with ``docker-compose``:

.. code-block::

    docker-compose up -d

The docker containers should be working now.

The docker directory in this tutorial is a slightly modified copy of the docker directory in the `core-java-spring <https://github.com/eclipse-arrowhead/core-java-spring>`_ repository.
My slight modifications fix some bugs from the ``master`` branch, but the ``docker-update`` branch works as far as I know.

Running the Management Tool
---------------------------

Next we want a way to monitor the local cloud, and for that we will use the Management Tool.
To run it, first pull the docker image:

.. code-block::

    docker pull svetlint/management-tool

Next, navigate to the ``management-tool`` directory

.. code-block::

    cd ../management-tool

and run the ``run-mgmt.sh`` script

.. code-block::

    ./run-mgmt.sh

Setting Up a Browser
--------------------

The management tool is a javascript application that runs in your browser, specifically Chromium based browsers.
It is accessed at the address `<http://172.17.0.1:3000>`_.

When you open it you will most likely see a page with some tabs that are all empty.
This is because even though we can access the management tool, and the management tool can access the core systems, because our browser lacks the certificates necessary to access the core systems, no information will be shown.
To fix this, we first need to add the certificates to our browser, which in Chromium is  ``settings > Privacy and security > Security > Manage certificates > import``.
In the import menu, navigate to the ``certificates/testcloud2`` repository and import ``sysop.p12``.

Now, visit the following three addresses: `<https://127.0.0.1:8443>`_, `<https://127.0.0.1:8441>`_, and `<https://127.0.0.1:8445>`_.
You will then be presented with a notification saying **Your connection is not private**.
We will promptly ignore this warning and click ``Advanced > Proceed to 127.0.0.1 (unsafe)`` and then choose the certificate named ``sysop.vaccine.ltu...`` in the menu that appears, and then press ok.
On each of the three addresses you will be presented with a SwaggerUI page.
We will come back to these later.
For now, go back to the management tool tab and refresh your browser.
The Service Registry tab should now contain about six services and two systems.

Now we have the local cloud up and running, and we can go on to using the Python library.





