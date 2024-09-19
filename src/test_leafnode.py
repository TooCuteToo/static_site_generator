import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_tag_value(self):
        leaf_node = LeafNode("This is a text node", tag="a")
        self.assertEqual(leaf_node.to_html(), "<a>This is a text node</a>")

    def test_to_html_tag_value_props(self):
        leaf_node = LeafNode(
            "This is a text node",
            tag="a",
            props={
                "href": "https://www.boot.dev",
                "target": "_blank",
            },
        )
        self.assertEqual(
            leaf_node.to_html(),
            '<a href="https://www.boot.dev" target="_blank">This is a text node</a>',
        )

    def test_require_value(self):
        leaf_node = LeafNode(None, tag="a")
        self.assertRaises(ValueError, leaf_node.to_html)

    def test_no_tag(self):
        leaf_node = LeafNode("This is a text node", None)
        self.assertEqual(leaf_node.to_html(), "This is a text node")


if __name__ == "__main__":
    unittest.main()
