
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-featherwing/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/featherwing/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing/actions/
    :alt: Build Status

This library provides FeatherWing specific classes for those that require a significant amount of
initialization.

Dependencies
=============
These drivers depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `INA219 <https://github.com/adafruit/Adafruit_CircuitPython_INA219>`_
* `Seesaw <https://github.com/adafruit/Adafruit_CircuitPython_seesaw>`_
* `HT16K33 <https://github.com/adafruit/Adafruit_CircuitPython_HT16K33>`_
* `DotStar <https://github.com/adafruit/Adafruit_CircuitPython_DotStar>`_
* `NeoPixel <https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel>`_
* `DS3231 <https://github.com/adafruit/Adafruit_CircuitPython_DS3231>`_
* `ST7735R <https://github.com/adafruit/Adafruit_CircuitPython_ST7735R>`_
* `ADXL34x <https://github.com/adafruit/Adafruit_CircuitPython_ADXL34x>`_
* `ADT7410 <https://github.com/adafruit/Adafruit_CircuitPython_ADT7410>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_ and highly recommended over
installing each one.

Installing from PyPI
--------------------

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-featherwing/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-featherwing

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-featherwing

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-featherwing

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_featherwing/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
