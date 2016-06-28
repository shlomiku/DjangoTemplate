#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    if os.environ.get('DEVELOPMENT_MODE', None):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.test')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
