# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.content.js.jquery.ui',
    version=version,
    description="jQuery Code.",
    long_description=open("README.rst").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.rst")).read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
        "Programming Language :: JavaScript",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: JavaScript Modules",
    ],
    keywords='javascript jQuery jQuery.UI',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://groupserver.org/',
    license='MIT',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.content', 'gs.content.js',
                        'gs.content.js.jquery'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'gs.content.js.jquery.base',
    ],
    extras_require={'zope': ['zope.browserresource', ]},
    entry_points="""
    # -*- Entry points: -*-
    """,)

