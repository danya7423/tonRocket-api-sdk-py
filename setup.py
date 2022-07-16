from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding = 'utf-8') as f:
    long_description = f.read()

setup(
    name = 'tonrocketapisdk',
    version = '1.0.0',
    packages = find_packages(),
    url = 'https://github.com/danya7423/tonRocket-api-sdk-py',
    license = 'MIT',
    author = 'я',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    install_requires = ['requests'],
    classifiers = ['Programming Language :: Python :: 3.6'],
)