#!/usr/bin/env python3.6

if __name__ == "__main__":
    import os, sys

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

