import unittest

from textnode import TextNode


class TestTextToTextNodes(unittest.TestCase):
    def test_text_with_link_image(self):
        text = "This is an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = TextNode.text_to_textnodes(text)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is an ", TextNode.text_type_text),
                TextNode(
                    "obi wan image",
                    TextNode.text_type_image,
                    "https://i.imgur.com/fJRm4Vk.jpeg",
                ),
                TextNode(" and a ", TextNode.text_type_text),
                TextNode("link", TextNode.text_type_link, "https://boot.dev"),
            ],
        )

    def test_text_with_all(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = TextNode.text_to_textnodes(text)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextNode.text_type_text),
                TextNode("text", TextNode.text_type_bold),
                TextNode(" with an ", TextNode.text_type_text),
                TextNode("italic", TextNode.text_type_italic),
                TextNode(" word and a ", TextNode.text_type_text),
                TextNode("code block", TextNode.text_type_code),
                TextNode(" and an ", TextNode.text_type_text),
                TextNode(
                    "obi wan image",
                    TextNode.text_type_image,
                    "https://i.imgur.com/fJRm4Vk.jpeg",
                ),
                TextNode(" and a ", TextNode.text_type_text),
                TextNode("link", TextNode.text_type_link, "https://boot.dev"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
