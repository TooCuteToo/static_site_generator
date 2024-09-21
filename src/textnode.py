from leafnode import LeafNode
import re


class TextNode:
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

    text_extract_pattern = {
        text_type_bold: r"(\*\*[^*]*\*\*)",
        text_type_italic: r"(\*[^*]*\*)",
        text_type_code: r"(`[^`]*`)",
    }

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_text_node):
        if self.text != other_text_node.text:
            return False

        if self.text_type != other_text_node.text_type:
            return False

        if self.url != other_text_node.url:
            return False

        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(text_node):
        if text_node.text_type == TextNode.text_type_text:
            return LeafNode(tag=None, value=text_node.text)

        if text_node.text_type == TextNode.text_type_bold:
            return LeafNode(tag="b", value=text_node.text)

        if text_node.text_type == TextNode.text_type_italic:
            return LeafNode(tag="i", value=text_node.text)

        if text_node.text_type == TextNode.text_type_code:
            return LeafNode(tag="code", value=text_node.text)

        if text_node.text_type == TextNode.text_type_link:
            return LeafNode(
                tag="a", value=text_node.text, props={"href": text_node.url}
            )

        if text_node.text_type == TextNode.text_type_link:
            return LeafNode(
                tag="img", value="", props={"src": text_node.url, "alt": text_node.text}
            )

        raise Exception(f"Invalid text type: {text_node.text_type}")

    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []

        for node in old_nodes:
            texts = re.split(TextNode.text_extract_pattern[text_type], node.text)

            for text in texts:
                if delimiter in text:
                    new_nodes.append(TextNode(text.replace(delimiter, ""), text_type))
                    continue

                if len(text) > 0:
                    new_nodes.append(TextNode(text, node.text_type))

        return new_nodes
