#!/usr/bin/python3
# vi:se ts=4 sts=4 et ai:

from setuptools import setup
from setuptools import find_packages
packages=find_packages('.')
print('find package:%s', packages)

setup(name='debhello',
    version='4.0',
    description='Hello Python',
    long_description='Hello Python program.',
    author='Osamu Aoki',
    author_email='osamu@debian.org',
    url='http://people.debian.org/~osamu/',
    packages=packages,
    package_dir={'hello_py': 'hello_py'},
    scripts=['scripts/hello'],
    classifiers = ['Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    entry_points = {
        'console_scripts': ['hello-version=hello_py.version:get_version'],
    },
    platforms   = 'POSIX',
    license     = 'MIT License'
)
