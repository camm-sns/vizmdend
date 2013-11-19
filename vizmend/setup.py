# vizmdend setup.py

from distutils.core import setup

setup(
    name = 'vizmdend',
    packages = ['vizmdend',],
    version = '1.1.0'
    description = 'AMBER mdend file inspector',
    author = 'Jose Borreguero',
    author_email = 'jose@borreguero.com',
    url = 'http://borreguero.com',
    url_download = 'http://borreguero.com',
    keywords = ['AMBER', 'mdend', 'energy', 'molecular dynamics'],
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 1 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: AMBER users',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Topic :: Modeling and Simulations :: Analysis :: Output Visualization',
        ],
    long_description = '''\
AMBER Molecular Dynamics mdend file Inspector
----------------------------------------------

This version requires Python 2.X > 2.4
'''
)
