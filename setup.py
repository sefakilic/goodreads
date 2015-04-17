from setuptools import setup
import pypandoc

setup(
    name = 'goodreads',
    description = "Python wrapper for Goodreads API",
    long_description = pypandoc.convert('README.md', 'rst'),
    author = 'Sefa Kilic',
    author_email = 'sefakilic@gmail.com',
    url = 'https://github.com/sefakilic/goodreads/',
    version = '0.2.0',
    install_requires = ['nose', 'xmltodict', 'requests', 'rauth'],
    packages = ['goodreads'],
    scripts = [],
    license = 'MIT',
)
