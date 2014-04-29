#!/bin/sh

coverage run \
    --omit="contacts/ft/*,contacts/user_contacts/tests/*,contacts/contacts/wsgi.py" \
    --source='contacts' \
    contacts/manage.py test user_contacts
coverage report