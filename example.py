#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
>>> import genuuid as _id
>>> uuid = _id.uuid()
>>> print("return uuid is '%s'." % uuid)
return uuid is 'p9KD3aSMEc8KAG2XCsoTA2'.
>>> print("Author is %s," % __author__, "Package Version is %s" % __version__)
Author is Lasha Gogua, Package Version is 0.1.0
"""

import genuuid as _id
from genuuid import __author__,__version__

uuid = _id.suuid()
uuid1 = _id.luuid() 
print("return uuid is '%s'. " % uuid, "uuid length is %s" % len(uuid))
print("return uuid is '%s'. " % uuid1, "uuid length is %s" % len(uuid1))
print("Author is %s," % __author__, "Package Version is %s" % __version__)