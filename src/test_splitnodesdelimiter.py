import unittest

from textnode import TextNode


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_block(self):
        node = TextNode(
            "This is text with a `code block` word", TextNode.text_type_text
        )
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextNode.text_type_code)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextNode.text_type_text, None),
                TextNode("code block", TextNode.text_type_code, None),
                TextNode(" word", TextNode.text_type_text, None),
            ],
        )

    def test_bold_block(self):
        node = TextNode(
            "This is text with a **bold block** word", TextNode.text_type_text
        )
        new_nodes = TextNode.split_nodes_delimiter(
            [node], "**", TextNode.text_type_bold
        )

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextNode.text_type_text, None),
                TextNode("bold block", TextNode.text_type_bold, None),
                TextNode(" word", TextNode.text_type_text, None),
            ],
        )

    def test_double_bold_block(self):
        node = TextNode(
            "This is text with a **bold block** word and **other bold block**",
            TextNode.text_type_text,
        )
        new_nodes = TextNode.split_nodes_delimiter(
            [node], "**", TextNode.text_type_bold
        )

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextNode.text_type_text, None),
                TextNode("bold block", TextNode.text_type_bold, None),
                TextNode(" word and ", TextNode.text_type_text, None),
                TextNode("other bold block", TextNode.text_type_bold, None),
            ],
        )

    def test_italic_block(self):
        node = TextNode(
            "This is text with a *italic block* word", TextNode.text_type_text
        )
        new_nodes = TextNode.split_nodes_delimiter(
            [node], "*", TextNode.text_type_italic
        )

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextNode.text_type_text, None),
                TextNode("italic block", TextNode.text_type_italic, None),
                TextNode(" word", TextNode.text_type_text, None),
            ],
        )

    def test_double_italic_block(self):
        node = TextNode(
            "This is text with a *italic block* word and *some other block*",
            TextNode.text_type_text,
        )
        new_nodes = TextNode.split_nodes_delimiter(
            [node], "*", TextNode.text_type_italic
        )

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextNode.text_type_text, None),
                TextNode("italic block", TextNode.text_type_italic, None),
                TextNode(" word and ", TextNode.text_type_text, None),
                TextNode("some other block", TextNode.text_type_italic, None),
            ],
        )


if __name__ == "__main__":
    unittest.main()
