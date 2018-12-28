#!/usr/bin/env python
"""
sentry-uaa-auth
==================
"""
from setuptools import setup, find_packages


install_requires = [
    'sentry>=7.0.0',
]

tests_require = [
    'flake8>=2.0,<2.1',
]

setup(
    name='sentry-uaa-auth',
    version='0.0.1',
    author='Kolya Opahle',
    author_email='kolyaopahle@gmail.com',
    url='https://www.github.com/Kolpa',
    description='Cloud Foundry UAA authentication provider for Sentry',
    long_description=__doc__,
    license='Apache 2.0',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'tests': tests_require},
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'uaa_auth = sentry_uaa_auth',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
