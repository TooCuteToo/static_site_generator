import unittest

from block_markdown import *


class TestBlockMarkdown(unittest.TestCase):
    def test_not_block_cases(self):
        str = "* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"

        blocks = BlockMarkdown.markdown_to_block(str)
        self.assertEqual(
            blocks,
            [
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ],
        )

    def test_block_cases(self):
        str = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"

        blocks = BlockMarkdown.markdown_to_block(str)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            ],
        )

    def test_block_to_block_heading_type(self):
        heading_block = [
            "## This is a heading",
            "# This is a heading",
            "#### This is a heading",
        ]
        for item in heading_block:
            self.assertEqual(
                BlockMarkdown.block_to_block_type(item),
                BlockMarkdown.block_type_heading,
            )

    def test_block_to_block_order_list_type(self):
        order_list_block = (
            "1. This is a heading\n2. This is a heading\n3. This is a heading"
        )

        self.assertEqual(
            BlockMarkdown.block_to_block_type(order_list_block),
            BlockMarkdown.block_type_ordered_list,
        )


if __name__ == "__main__":
    unittest.main()
