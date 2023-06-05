from setuptools import setup, find_packages

setup(
    name='minihit',
    version='1.0',
    description='A Python project for minimum hitting set calculations.',
    packages=find_packages(),
    install_requires=[
        'graphviz',
    ],
)

