# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='agronomy',
    version=version,
    description='App for managing Crop Trials',
    author='Mayur Patel',
    author_email='mike_mayur@hotmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
