# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.0'


setup(
    name='django-shortcuts',
    version=version,
    keywords='Django ShortCuts',
    description='Django ShortCuts',
    long_description=open('README.rst').read(),

    url='https://github.com/django-xxx/django-shortcuts',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['django_shortcuts'],
    py_modules=[],
    install_requires=['django-json-render'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
