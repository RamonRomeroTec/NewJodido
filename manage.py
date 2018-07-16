#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    #por si la cago
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deajodido.settings")
    if os.path.isfile('/etc/secret_key.txt'):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deajodido.settings.production")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deajodido.settings.development")
    print(os.environ['DJANGO_SETTINGS_MODULE'])

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
