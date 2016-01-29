#!/usr/bin/env python

import sys
from distutils.core import setup
from genuuid import __version__, __author__
assert sys.version >= "2.7", "Requires Python v2.7 and v2.7.x or above versions."

setup (
	name = "genuuid",
	version = __version__,
	description = "Simple Generate UUID (Universal Unique Identification)",
	author = __author__,
	author_email = "Lh4cKg@gmail.com",
	url = "https://github.com/Lh4cKg/simple-generator-uuid/",
	packages = ["genuuid"],
	classifiers=[
		"Development Status :: Beta",
		"Environment :: Console",
		"Environment :: Web Environment",
		"License :: OSI Approved :: Python Software Foundation License",
		"Operating System :: POSIX :: Linux",
		"Operating System :: MacOS :: MacOS X",
		"Operating System :: Microsoft :: Windows",
		"Programming Language :: Python",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3.0",
		"Programming Language :: Python :: 3.1",
		"Programming Language :: Python :: 3.2",
		"Programming Language :: Python :: 3.3",
		"Programming Language :: Python :: 3.4",
		"Programming Language :: Python :: 3.5",
		"Topic :: Software Development :: Libraries :: Python Modules",
          ],
)