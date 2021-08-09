Template for Launching an ML App in a FastAPI Server
####################################################

This repo is a template for taking a machine learning model 
and mock-deploying it in a local docker container using `FastAPI <https://fastapi.tiangolo.com/>`_.

Usage
=====

I hope to make this into a `Cookiecutter <https://cookiecutter.readthedocs.io/en/1.7.3/>`_ template one day, but until then use it by modifying 
the parts you need by hand.

Install
-------

For sending data, install the client requirements:

.. code::
    
    pip install -r requirements/client.py


Optionally, if you want to use datagen to make your Pydantic data models, 

.. code::

    pip install -r "requirements/client.txt[datagen]"

Description
===========

Everything under the :code:`app` directory is related to the docker container. 
The :code:`main.py` script is concerned with the FastAPI app itself, and the :code:`app.model.py` 
file is the place for you to insert the code that will run your model.


Generate the Data Model
----------------------------------

Since this is built with FastAPI, you can specify a `Pydantic <https://pydantic-docs.helpmanual.io/>`_ data model for 
requests to this app. See the next session if you want a quick way to do it, or you can do it manually.
If you have a pydantic data model setup for your model input, go ahead and use that. 
Optionally, you can use `datamodel-code-generator <https://github.com/koxudaxi/datamodel-code-generator/>`_ to generate one from a :code:`sample_data.json` file:

.. code::

    make data_model

Then just read over the generated python script and double-check it matches what you are expecting.


Launching
=========

Locally
-------

If you want to launch the uvicorn server without docker, use

.. code::

    make server


and it will run the app with uvicorn.

In Docker
---------

When you're ready to make it a docker container, build the image and run the container with 

.. code::

    make docker


Send Data to the Model
======================

You can modify the :code:`send_data.py` script as needed to send data to the model.
If you wish, you can use :code:`make send` to run the script.



