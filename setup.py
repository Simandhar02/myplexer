#!/usr/bin/env python

from setuptools import setup
import pip


# do not change redis library version
setup(
    name='myplexer',
    version='0.1',
    description='MyPlexer Library for assignment',
    author='Simandhar Sahuji',
    author_email='simandar.sahuji@gmail.com',
    url='https://git.txtbox.in:8080/smcore/sm_utils',
    packages=['myplexer'],
    install_requires=[
        'Flask==1.0.2'
    ]
)

# # main is moved to _internal module in pip version 10.0.0
# pip_version = pip.__version__.split(".")[0]
# if int(pip_version) >= 10:
#     from pip._internal import main
# else:
#     from pip import main
