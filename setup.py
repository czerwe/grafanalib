from setuptools import setup

import grafanalib

setup(
    name='grafanalib',
    version=grafanalib.__version__,
    packages=['grafanalib'],
    install_requires=['requests>=2.8.1', 'click>=6.6'],
    setup_requires=['requests>=2.8.1', 'click>=6.6']
)