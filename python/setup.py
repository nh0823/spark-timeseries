from setuptools import setup, find_packages
import os

VERSION = '0.2.0-SNAPSHOT'
JAR_FILE = 'sparkts-' + VERSION + '-jar-with-dependencies.jar'

setup(
    name='sparkts',
    description = 'A library for analyzing large time series data with Apache Spark',
    author = 'Sandy Ryza',
    author_email = 'sandy@cloudera.com',
    url = 'https://github.com/sryza/spark-timeseries',
    version=VERSION,
    packages=find_packages(),
    include_package_data = True,
    classifiers = [],
    keywords = ['spark', 'time', 'series', 'data', 'analysis'],
    install_requires = [
        'pandas >= 0.13',
        'numpy >= 1.9.2'
    ],
    test_requires = [
        'nose == 1.3.7',
        'unittest2 >= 1.0.0'
    ]
)
