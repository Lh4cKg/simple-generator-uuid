===========
Description
===========

``genuuid`` is simple generate UUID(Universal Unique Identification).

Installation Requirements
-----------------------------------

* Python 2.7, 3.3, 3.4, 3.5
* To install the source, download it from https://github.com/Lh4cKg/simple-generator-uuid and do ``python setup.py install``.

To install ``genuuid``::

    $ git clone https://github.com/Lh4cKg/simple-generator-uuid "genuuid"
    $ cd genuuid
    $ sudo python setup.py install

Usage
---------

To use ``genuuid``, just import it in your project like so:

>>> import genuuid as _id

You can then generate a long and short combined UUID:

>>> _id.luuid()
'6ncYfoH6AT8LBhZQBii0Zr'
>>> _id.suuid()
'LSJQKhGKH8E'

Create a simple function::

    def long_uuid():
           """
           long uuid
           """
           return _id.luuid()

    def short_uuid():
           """
           short uuid
           """
           return _id.suuid()

>>> long_uuid()
'LwJiUC63Nc8778SDJHm3b'
>>> short_uuid()
'koZiFTGnWJ1'

Contributing
-----------------
There are plenty of ways to contribute to this project. If you think you’ve found a bug please submit an issue.