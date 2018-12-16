from setuptools import setup, find_packages
from os import path

setup(
    name='Mario',
    version='1.0.0',
    description='Simulation of basic mario game',
    author='Anchit Gupta',
    author_email='anchit.gupta@research.iiit.ac.in',
    keywords='Mario',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)