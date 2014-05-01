from os.path import dirname, realpath

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

from django.test import LiveServerTestCase


class LiveValidationTestCase(LiveServerTestCase):
    """
    run tests on ajaxy live validation
    """

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def key(self, name, keys):
        self.by('name', name).send_keys(keys)

    def by(self, what, key):
        get = getattr(self.browser, 'find_element_by_' + what)
        return get(key)

    def test_validation_avatar_appears(self):
        self.browser.get(self.live_server_url + "/add")
        self.key('first_name', 'a')

        self.assertIsInstance(
            self.by('id', 'validate_avatar_id_first_name'),
            WebElement)

        self.assertEqual(
            self.by('id', 'validate_avatar_id_first_name').tag_name,
            'span')

    def test_validation_ajax_runs(self):
        self.browser.get(self.live_server_url + "/add")
        self.key('first_name', 'a')

        for ii in xrange(5):
            notActive = self.browser.execute_script("return $.active == 0")
            if notActive:
                break
            sleep(.5)

        self.assertIsInstance(
            self.by('id', 'validate_avatar_id_first_name'),
            WebElement)

        self.assertEqual(
            self.by('id', 'validate_avatar_id_first_name').text,
            'valid')

    def test_invalid_first_name(self):
        self.browser.get(self.live_server_url + "/add")
        self.key('first_name', 'a+')

        for ii in xrange(5):
            notActive = self.browser.execute_script("return $.active == 0")
            if notActive:
                break
            sleep(.5)

        self.assertIsInstance(
            self.by('id', 'validate_avatar_id_first_name'),
            WebElement)

        self.assertEqual(
            self.by('id', 'validate_avatar_id_first_name').text,
            'Invalid: something other than letters or is empty')

    def test_invalid_address(self):
        self.browser.get(self.live_server_url + "/add")
        self.key('address', 'a+')

        for ii in xrange(5):
            notActive = self.browser.execute_script("return $.active == 0")
            if notActive:
                break
            sleep(.5)

        self.assertIsInstance(
            self.by('id', 'validate_avatar_id_address'),
            WebElement)

        self.assertEqual(
            self.by('id', 'validate_avatar_id_address').text,
            'Invalid: Street Address Must Contain Number')
