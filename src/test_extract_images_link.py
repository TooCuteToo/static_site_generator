import unittest

from textnode import TextNode


class TestExtractImageLink(unittest.TestCase):
    def test_extract_single_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(
            TextNode.extract_markdown_images(text),
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif")],
        )

    def test_extract_multiple_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and ![persona 3](https://gamelade.vn/wp-content/uploads/2024/02/Persona-3-reload-preview-header.webp)"
        self.assertEqual(
            TextNode.extract_markdown_images(text),
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
                (
                    "persona 3",
                    "https://gamelade.vn/wp-content/uploads/2024/02/Persona-3-reload-preview-header.webp",
                ),
            ],
        )

    def test_extract_invalid_images_with_links(self):
        text = "This is text with a [to boot dev](https://www.boot.dev) and [google](https://www.google.com) and [steam](https://www.steampowered.com)"
        self.assertEqual(
            TextNode.extract_markdown_images(text),
            [],
        )

    def test_extract_images_mix_with_links(self):
        text = "This is text with a [to boot dev](https://www.boot.dev) and [google](https://www.google.com) and [steam](https://www.steampowered.com) and ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(
            TextNode.extract_markdown_images(text),
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif")],
        )

    def test_extract_single_link(self):
        text = "This is text with a [to boot dev](https://www.boot.dev)"
        self.assertEqual(
            TextNode.extract_markdown_link(text),
            [("to boot dev", "https://www.boot.dev")],
        )

    def test_extract_multiple_links(self):
        text = "This is text with a [to boot dev](https://www.boot.dev) and [google](https://www.google.com) and [steam](https://www.steampowered.com)"
        self.assertEqual(
            TextNode.extract_markdown_link(text),
            [
                ("to boot dev", "https://www.boot.dev"),
                ("google", "https://www.google.com"),
                (
                    "steam",
                    "https://www.steampowered.com",
                ),
            ],
        )

    def test_extract_links_mix_with_images(self):
        text = "This is text with a [to boot dev](https://www.boot.dev) and [google](https://www.google.com) and ![steam](https://www.steampowered.com)"
        self.assertEqual(
            TextNode.extract_markdown_link(text),
            [
                ("to boot dev", "https://www.boot.dev"),
                ("google", "https://www.google.com"),
            ],
        )

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextNode.text_type_text,
        )
        new_nodes = TextNode.split_nodes_link([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", TextNode.text_type_text),
                TextNode(
                    "to boot dev", TextNode.text_type_link, "https://www.boot.dev"
                ),
                TextNode(" and ", TextNode.text_type_text),
                TextNode(
                    "to youtube",
                    TextNode.text_type_link,
                    "https://www.youtube.com/@bootdotdev",
                ),
            ],
        )

    def test_split_nodes_link_mix_image(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextNode.text_type_text,
        )
        new_nodes = TextNode.split_nodes_link([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", TextNode.text_type_text),
                TextNode(
                    "to boot dev", TextNode.text_type_link, "https://www.boot.dev"
                ),
                TextNode(
                    " and ![to youtube](https://www.youtube.com/@bootdotdev)",
                    TextNode.text_type_text,
                ),
            ],
        )

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with a image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextNode.text_type_text,
        )
        new_nodes = TextNode.split_nodes_image([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a image ", TextNode.text_type_text),
                TextNode(
                    "to boot dev", TextNode.text_type_image, "https://www.boot.dev"
                ),
                TextNode(" and ", TextNode.text_type_text),
                TextNode(
                    "to youtube",
                    TextNode.text_type_image,
                    "https://www.youtube.com/@bootdotdev",
                ),
            ],
        )

    def test_split_nodes_images_mix_link(self):
        node = TextNode(
            "This is text with a image ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextNode.text_type_text,
        )
        new_nodes = TextNode.split_nodes_image([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a image ", TextNode.text_type_text),
                TextNode(
                    "to boot dev", TextNode.text_type_image, "https://www.boot.dev"
                ),
                TextNode(
                    " and [to youtube](https://www.youtube.com/@bootdotdev)",
                    TextNode.text_type_text,
                ),
            ],
        )

    def test_split_nodes_image_no_image(self):
        node1 = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextNode.text_type_text,
        )

        node2 = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextNode.text_type_text,
        )

        new_nodes = TextNode.split_nodes_image([node1, node2])

        self.assertEqual(
            new_nodes,
            [
                TextNode(
                    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                    TextNode.text_type_text,
                ),
                TextNode(
                    "This is text with a link [to boot dev](https://www.boot.dev) and ",
                    TextNode.text_type_text,
                ),
                TextNode(
                    "to youtube",
                    TextNode.text_type_image,
                    "https://www.youtube.com/@bootdotdev",
                ),
            ],
        )


if __name__ == "__main__":
    unittest.main()
