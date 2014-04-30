#!/usr/bin/env bash

CWD=$(pwd)
RESULT=0;
while read ln; do
    pep8 "$CWD/$ln"
    RESULT=$(( $RESULT + $?))
done < <(git ls-tree -r master --name-only | grep ".*py$")

exit $RESULT