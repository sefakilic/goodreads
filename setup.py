from setuptools import setup

setup(
    name='goodreads',
    description="Python wrapper for Goodreads API",
    long_description=open("README.rst").read(),
    url='https://github.com/sefakilic/goodreads/',
    
    author='Sefa Kilic',
    author_email='sefakilic@gmail.com',

    packages=['goodreads'],
    version='0.3.1',
    install_requires=['nose', 'xmltodict', 'requests', 'rauth'],

    license='MIT',

    keywords = 'goodreads API',

    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
    ]
    
)
