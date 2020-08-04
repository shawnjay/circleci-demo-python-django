#!/usr/bin/env python
import os
import sys
import subprocess

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locallibrary.settings")
    try:
        from django.core.management import execute_from_command_line
        sysCmdStr = """curl -H "Content-Type: application/graphql+-" "40.64.83.71:8080/query" -XPOST -d $'
        {
          node(func: uid(0xb31f36)) {
            uid
            expand(_all_) {
              uid
              expand(_all_)
            }
          }
        }
        ' | python -m json.tool | less"""
        ret = subprocess.check_output(sysCmdStr, shell=True)
        print("step1: ret = ", ret)
        if ret == None:
            raise Exception("step1: ret is None")
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
            print("step2: abc")
            raise Exception("step2: test raise exception for circleci")
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
