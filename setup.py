# from aptk.__version__ import release
import sys, os

from setuptools import setup, find_packages

long_desc = '''
This package contains tools for easy sphinx domain creation.
'''

sys.path.insert(0, 'sphinxcontrib')

requires = ['sphinx>=1.4']

setup(
    name='sphinxcontrib-domaintools',
    version='0.1',
    url='http://bitbucket.org/klorenz/sphinxcontrib-domaintools',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-domaintools',
    license='BSD',
    author='Kay-Uwe (Kiwi) Lorenz',
    author_email='kiwi@franka.dyndns.org',
    description='Sphinx extension for easy domain creation.',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
