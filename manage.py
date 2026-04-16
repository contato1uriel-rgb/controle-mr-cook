#!/usr/bin/env python
"""manage.py na raiz: migrate/collectstatic em CI e hosts que esperam isto na raiz."""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTROLE = os.path.join(ROOT, "controle")
sys.path.insert(0, CONTROLE)
os.chdir(CONTROLE)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "controle.settings")


def main():
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
