#!/bin/sh

coverage run \
    --omit="contacts/ft/*,contacts/user_contacts/tests/*" \
    --source='contacts' \
    contacts/manage.py test user_contacts
coverage report