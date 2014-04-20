#!/usr/bin/env python

from subprocess import call

if __name__ == '__main__':
    errs = call(["python", "manage.py", "test", "ft"])
    exit(errs)
