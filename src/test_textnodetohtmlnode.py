import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_text_node_to_text(self):
        text_node = TextNode(
            text_type=TextNode.text_type_text, text="This is a text node text"
        )

        html_node = TextNode.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "This is a text node text")

    def test_text_node_to_bold(self):
        text_node = TextNode(
            text_type=TextNode.text_type_bold, text="This is a text node bold"
        )

        html_node = TextNode.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>This is a text node bold</b>")

    def test_text_node_to_italic(self):
        text_node = TextNode(
            text_type=TextNode.text_type_italic, text="This is a text node italic"
        )

        html_node = TextNode.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>This is a text node italic</i>")

    def test_invalid_text_node(self):
        text_node = TextNode(text_type="paragaph", text="This is a text node italic")

        self.assertRaises(Exception, TextNode.text_node_to_html_node)


if __name__ == "__main__":
    unittest.main()
