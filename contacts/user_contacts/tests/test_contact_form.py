from django.test import TestCase

from user_contacts.models import Person
from user_contacts.new_contact_form import ContactForm


class TestContactForm(TestCase):
    def test_if_valid_contact_is_saved(self):
        data = {
            'first_name': 'test',
            'last_name': 'test',
            'number': '123450000'}

        form = ContactForm(data)
        form.save()

    def test_if_invalid_contact_is_not_saved(self):
        data = {
            'first_name': 'tes&t',
            'last_name': 'test',
            'number': '83883333'}
        form = ContactForm(data)
        contact = form.save()
        self.assertEquals(contact, None)
