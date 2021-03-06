from django.core.exceptions import ValidationError
from django.test import TestCase

from user_contacts.validators import (
    validate_number,
    validate_string,
    validate_address)


class ValidatorTest(TestCase):
    def test_string_is_invalid_if_contains_numbers_or_special_chars(self):
        with self.assertRaises(ValidationError):
            validate_string('@test')
            validate_string('tester#')

    def test_number_is_invalid_if_contains_non_digit(self):
        with self.assertRaises(ValidationError):
            validate_number('1234ABC')
            validate_number('1234#')

    def test_address_contains_number(self):
        with self.assertRaises(ValidationError):
            validate_address("Fake St")
