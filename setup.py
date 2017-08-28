#     Copyright (C) 2017
#
#     Copying and distribution of this file, with or without modification,
#     are permitted in any medium without royalty provided the copyright
#     notice and this notice are preserved.  This file is offered as-is,
#     without any warranty.

from setuptools import setup, find_packages

packages=find_packages()

setup(
    name="caslib",
    version='1.0.0',
    # uncomment the following lines if you fill them out in release.py
    description='caslib provides a python interface to CAS',
    author='Nicolas gibelin',
    author_email='Nicolas.Gibelin@univ-grenoble-alpes.fr',
    url='https://github.com/nicolas-gibelin/caslib',
    license='LGPL',

    install_requires=[
    ],

    extras_require=dict(
	# Earlier versions untested
	HTML=["lxml >= 2.2"],

	certificate_validation=[
	# Require Python 3
	    "Python >= 3.0",
	],
    ),

    # Probably?  Not tested.
    zip_safe=False,
    packages=packages,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
	'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    ],
    # test_suite='nose.collector',
)
