import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq_bold(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_italic(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "italic")
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", "italic")
        self.assertEqual(node.url, None)

    def test_not_eq(self):
        node = TextNode("This is a text node 1", "italic")
        node2 = TextNode("This is a text node 2", "italic")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node 1", "italic")
        self.assertEqual("TextNode(This is a text node 1, italic, None)", repr(node))


if __name__ == "__main__":
    unittest.main()
