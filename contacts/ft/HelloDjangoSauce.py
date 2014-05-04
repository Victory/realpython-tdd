import os
import sys
import unittest
import sauceclient

from selenium import webdriver
from django.test import LiveServerTestCase

from sauceclient import SauceClient


USERNAME = "Victory"
ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

sauce = SauceClient(USERNAME, ACCESS_KEY)

browsers = [{"platform": "Mac OS X 10.9",
             "browserName": "chrome",
             "version": ""},
            {"platform": "Windows 8.1",
             "browserName": "internet explorer",
             "version": "11"}]


def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = type(name, (base_class,), d)
    return decorator


@on_platforms(browsers)
class SaucheTest(LiveServerTestCase):

    def setUp(self):
        self.caps['name'] = self.id()
        self.caps['tunnel-identifier'] = os.environ['TRAVIS_JOB_NUMBER']
        self.caps['build'] = os.environ['TRAVIS_BUILD_NUMBER']
        self.caps['tags'] = [os.environ['TRAVIS_PYTHON_VERSION'], 'CI']

        print self.caps

        sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
        self.driver = webdriver.Remote(
            desired_capabilities=self.caps,
            command_executor=sauce_url % (USERNAME, ACCESS_KEY)
        )
        self.driver.implicitly_wait(30)

    def tearDown(self):
        print("Link to your job: "
              "https://saucelabs.com/jobs/%s" % self.driver.session_id)
        try:
            if sys.exc_info() == (None, None, None):
                sauce.jobs.update_job(self.driver.session_id, passed=True)
            else:
                sauce.jobs.update_job(self.driver.session_id, passed=False)
        finally:
            self.driver.quit()

    def test_sauce(self):
        self.driver.get('http://localhost:8000/')
        assert "I am a page title - Sauce Labs" in self.driver.title
