from django.test import TestCase
from user_contacts.models import (
    Person,
    Phone)


class PersonTest(TestCase):
    def test_unicode(self):
        person = Person()
        first_name = "fred"
        last_name = "smith"
        person.first_name = first_name
        person.last_name = last_name
        expected = "%s, %s" % (last_name, first_name)
        actual = person.__unicode__()
        self.assertEquals(expected, actual)


class PhoneTest(TestCase):

    def test_unicode(self):
        phone = Phone()
        number = "8675309"
        phone.number = number

        expected = number
        actual = phone.__unicode__()
        self.assertEquals(expected, actual)
