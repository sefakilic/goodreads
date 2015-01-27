from distutils.core import setup

config = {
    'description': 'Python wrapper for Goodreads API',
    'author': 'Sefa Kilic',
    'url': 'https://github.com/sefakilic/goodreads/',
    'author_email': 'sefakilic@gmail.com',
    'version': '0.1',
    'install_requires': ['nose',
                         'xmltodict',
                         'requests',
                         'rauth'],
    'packages': ['goodreads'],
    'scripts': [],
    'name': 'goodreads'
}

setup(**config)
