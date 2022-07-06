from distutils.core import setup
from setuptools import setup, find_packages

cmd_name = "icli"

setup(name='isi-cli',
      version='1.0',
      description='General purpose CLI',
      author='Isidro Lopez',
      author_email='islomar@gmail.com',
      url="https://github.com/poc-cli/icli",
      license="Apache License 2.0",
      packages=find_packages(exclude=["tests.*", "tests"]),
     )