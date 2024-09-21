import unittest

from textnode import TextNode


class TestSplitNodesDelimiter(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
