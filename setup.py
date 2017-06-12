from setuptools import setup

import grafanalib

setup(
    name='grafanalib',
    version=grafanalib.__version__,
    packages=['grafanalib'],
    test_suite="tests",
    install_requires=['requests>=2.8.1'],
    setup_requires=['requests>=2.8.1']
)