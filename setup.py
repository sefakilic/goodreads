from setuptools import setup
import pypandoc

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(
    name = 'goodreads',
    description = "Python wrapper for Goodreads API",
    long_description = read_md("README.md")
    author = 'Sefa Kilic',
    author_email = 'sefakilic@gmail.com',
    url = 'https://github.com/sefakilic/goodreads/',
    version = '0.2.2',
    install_requires = ['nose', 'xmltodict', 'requests', 'rauth'],
    packages = ['goodreads'],
    scripts = [],
    license = 'MIT',
)
