"""
=====================
Django Template Hooks
=====================

Provides template hooks to provide an easy interface for pluggable apps to
extend your templates.

:copyright: 2010, Pascal Hartig <phartig@weluse.de>
:license: BSD, see LICENSE for more details
"""

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup


setup(
    name='django-templatehooks',
    version='0.5.1',
    author='Pascal Hartig',
    author_email='phartig@weluse.de',
    packages=['templatehooks', 'templatehooks.templatetags'],
    url='http://github.com/weluse/django-templatehooks',
    license='BSD',
    description='Template hooks for django',
    long_description=__doc__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.6",
        "Framework :: Django",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    zip_safe=False
)
