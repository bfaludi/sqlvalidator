
from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name = 'sqlvalidator',
    version = version,
    description = "Generates Validation SQL",
    packages = find_packages( exclude = [ 'ez_setup'] ),
    include_package_data = True,
    zip_safe = False,
    author = 'Bence Faludi',
    author_email = 'bence@ozmo.hu',
    license = 'GPL',
    install_requires = [],
    test_suite = "sqlvalidator.tests",
    url = 'http://bfaludi.com',
    entry_points = """\
        [console_scripts]
        generate-validate-sql = sqlvalidator:main
    """
)