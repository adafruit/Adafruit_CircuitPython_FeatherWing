
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-featherwing/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/featherwing/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

This library provides FeatherWing specific classes for those that require a significant amount of
initialization.

Dependencies
=============
These drivers depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `PCA9685 <https://github.com/adafruit/Adafruit_CircuitPython_PCA9685>`_
* `Motor <https://github.com/adafruit/Adafruit_CircuitPython_Motor>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_ and highly recommended over
installing each one.

API Reference
=============

.. toctree::
   :maxdepth: 2

   api

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_featherwing/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-featherwing --library_location .
