"""
=====================
Django Template Hooks
=====================

Provides template hooks to provide an easy interface for pluggable apps to
extend your templates.
"""

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

setup(
    name='django-templatehooks',
    version='0.1.1',
    author='Pascal Hartig',
    author_email='phartig@weluse.de',
    packages=['templatehooks', 'templatehooks.templatetags'],
    url='http://github.com/weluse/django-templatetags',
    license='MIT',
    description='Template hooks for django',
    long_description=__doc__,
    zip_safe=False
    # test_suite='still to be written'
)
