import unittest

from helper import Helper


class TestHelper(unittest.TestCase):
    def test_extract_title_hello(self):
        title = Helper.extract_title("# Hello")
        self.assertEqual(title, "Hello")

    def test_extract_title_h2(self):
        self.assertRaises(ValueError, Helper.extract_title, "## Hello")
