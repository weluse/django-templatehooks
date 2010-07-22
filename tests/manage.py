#!/usr/bin/env python
# pylint: disable=W0403
import os
import sys

from django.conf import settings
from django.core.management import setup_environ, execute_from_command_line


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    import settings as settings_mod  # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the "
    "directory containing %r. It appears you've customized things.\n"
    "You'll have to run django-admin.py, passing it your settings module.\n"
    "(If the file settings.py does indeed exist, it's causing an ImportError "
    "somehow.)\n" % __file__)
    sys.exit(1)

# setup the environment before we start accessing things in the settings.
setup_environ(settings_mod)

if __name__ == "__main__":
    execute_from_command_line()
