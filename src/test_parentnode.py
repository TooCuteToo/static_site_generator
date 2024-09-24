import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_children_node_is_leafnode(self):
        node = ParentNode(
            "p",
            children=[
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_children_node_is_none(self):
        node = ParentNode(
            "p",
            children=None,
        )

        self.assertRaises(
            ValueError,
            node.to_html,
        )

    def test_parent_node_tag_none(self):
        node = ParentNode(
            None,
            None,
        )

        self.assertRaises(ValueError, node.to_html)

    def test_parent_node_tag_emtpy(self):
        node = ParentNode(
            "",
            None,
        )

        self.assertRaises(ValueError, node.to_html)

    def test_children_is_parent_node(self):
        node = ParentNode(
            "div",
            children=[
                ParentNode(
                    tag="p",
                    children=[
                        LeafNode(tag="b", value="Bold text"),
                        LeafNode(tag=None, value="Normal text"),
                        LeafNode(tag="i", value="italic text"),
                        LeafNode(tag=None, value="Normal text"),
                    ],
                ),
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ],
        )

        self.assertEqual(
            "<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</div>",
            node.to_html(),
        )

    def test_children_with_props(self):
        node = ParentNode(
            "div",
            children=[
                ParentNode(
                    tag="p",
                    children=[
                        LeafNode(
                            tag="b", value="Bold text", props={"fontsize": "12px"}
                        ),
                        LeafNode(tag=None, value="Normal text"),
                        LeafNode(
                            tag="i", value="italic text", props={"fontsize": "2rem"}
                        ),
                        LeafNode(tag=None, value="Normal text"),
                    ],
                    props={"padding": "5rem"},
                ),
                LeafNode(tag="b", value="Bold text", props={"fontsize": "12px"}),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text", props={"fontsize": "2rem"}),
                LeafNode(tag=None, value="Normal text"),
            ],
            props={
                "margin": "auto",
            },
        )

        self.assertEqual(
            '<div margin="auto"><p padding="5rem"><b fontsize="12px">Bold text</b>Normal text<i fontsize="2rem">italic text</i>Normal text</p><b fontsize="12px">Bold text</b>Normal text<i fontsize="2rem">italic text</i>Normal text</div>',
            node.to_html(),
        )


if __name__ == "__main__":
    unittest.main()
