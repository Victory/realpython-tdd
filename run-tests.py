#!/usr/bin/env python

import argparse
import os

from subprocess import call

from pyvirtualdisplay import Display

try:
    fh = open(os.path.dirname(os.path.realpath(__file__)) + '/sauce-key.txt')
    key = fh.read().strip()
    os.environ.setdefault('SAUCE_ACCESS_KEY', key)
except:
    if not os.environ.get('SAUCE_ACCESS_KEY'):
        print "Warning Sauce Key Not Read"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Tests for TDD')
    parser.add_argument(
        '-v', '--virtual',
        help="Use Virtual Display", action="store_true")
    args = parser.parse_args()

    if args.virtual:
        display = Display(visible=0, size=(1440, 900))
        display.start()

    errs = 0

    saucetest = ['ft.HelloSauce',
                 'ft.HelloDjangoSauce']
    for test in saucetest:
        print "running '%s'" % test
        err = call(["python", "contacts/manage.py", "test", test])
        if err:
            print "Failed\n"
        else:
            print "Passed\n"
        errs += err

    tests = ['ft.tests', 'ft.livevalidation', "user_contacts"]
    for test in tests:
        print "running '%s'" % test
        err = call(["python", "contacts/manage.py", "test", test])
        if err:
            print "Failed\n"
        else:
            print "Passed\n"
        errs += err

    errs += call(["/usr/bin/env", "bash", "./pep8.sh"])

    exit(errs)
