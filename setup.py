import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "memcache_wrapper",
    version = "1.0.0",
    packages=find_packages(exclude=["test", "test.*"]),

    install_requires = ['mockito', 'mockcache', 'python-memcached'],

    # metadata for upload to PyPI
    author = "xwhuang",
    author_email = "xwhuang@qnap.com",
    description=('A Python function wrapper to cache method results '
                 'using memcache'),
    long_description=read('README'),
    classifiers=[
        "Topic :: Utilities"
    ]
)