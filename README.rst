Template for Launching an ML App in a FastAPI Server
####################################################

This repo is a template for taking a machine learning model 
and mock-deploying it in a local docker container using FastAPI.

Description
===========

Everything under the :code:`app` directory is related to the docker container. 
The :code:`main.py` script is concerned with the FastAPI app itself, and the :code:`app.model.py` 
file is the place for you to insert the code that will run your model.


Generate the Data Model
----------------------------------

Since this is built with FastAPI, you can specify a Pydantic data model for 
requests to this app. See the next session if you want a quick way to do it, or you can do it manually.
If you have a pydantic data model setup for your model input, go ahead and use that. 
Optionally, you can use :code:`datamodel-code-generator` to generate one from a :code:`sample_data.json` file:

.. code::

    pip install -r "requirements/client.txt[datagen]"
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

..code::

    make docker


Send Data to the Model
======================

You can modify the :code:`send_data.py` script as needed to send data to the model.
If you wish, you can use :code:`make send` to run the script.



