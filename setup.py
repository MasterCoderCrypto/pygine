import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

setup(
name='pygine', 
version='1.0',
py_modules = ['farbkonstanten.py'],
scripts = [],
author= '"Marvin Maerz", "Jacob Behrendt", "Paul Walcher", "Thassilo Horn"',
long_description = '',
package_dir = {"", "src"},
packages = find_packages()
)
