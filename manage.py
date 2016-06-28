#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    if os.environ.get('CONTINIOUS_INTEGRATION', None):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.test')
    else:
        # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
        print "CONTINIOUS_INTEGRATION: "
        print os.environ.get('CONTINIOUS_INTEGRATION', None)
        print ", ".join(os.environ.keys())
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.test')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
