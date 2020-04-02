from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='MariadbAbcLog',

    version='1.1.0',

    description='Stored Routines (for MySQL and MariaDB) for logging',
    long_description=long_description,

    url='https://github.com/PhpPlaisio/sp-log',

    author='Set Based IT Consultancy',
    author_email='info@setbased.nl',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Code Generators',
        'Topic :: System :: Installation/Setup',

        'Programming Language :: SQL',

        'License :: OSI Approved :: MIT License'
    ],

    keywords='stored routines, logging,  mysql, MariaDB',

    packages=['MariadbAbcLog'],
    package_dir={'MariadbAbcLog': '.'},
    package_data={'MariadbAbcLog': ['lib/psql/abc_log/*.psql']}
)
