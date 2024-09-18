import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_a_tag_props(self):
        node = HTMLNode(
            tag="a",
            value="This is a html node",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(
            'href="https://www.google.com" target="_blank"', node.props_to_html()
        )

    def test_p_tag_props(self):
        node = HTMLNode(
            tag="p",
            value="This is p html node",
            props={
                "custom_tag_1": "Value of custom tag 1",
                "custom_tag_2": "Value of custom tag 2",
            },
        )
        self.assertEqual(
            'custom_tag_1="Value of custom tag 1" custom_tag_2="Value of custom tag 2"',
            node.props_to_html(),
        )

    def test_repr(self):
        node = HTMLNode(tag="p", value="This is p html node", children=None, props=None)
        self.assertEqual("HTMLNode(p, This is p html node, None, None)", repr(node))


if __name__ == "__main__":
    unittest.main()
