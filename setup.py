from setuptools import setup

setup(
    name='goodreads',
    description="Python wrapper for Goodreads API",
    long_description=open("README.rst").read(),
    author='Sefa Kilic',
    author_email='sefakilic@gmail.com',
    url='https://github.com/sefakilic/goodreads/',
    version='0.2.4',
    install_requires=['nose', 'xmltodict', 'requests', 'rauth'],
    packages=['goodreads'],
    scripts=[],
    license='MIT',
)
