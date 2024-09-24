from block_markdown import BlockMarkdown
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode


class Helper:
    def markdown_to_html_node(markdown):
        blocks = BlockMarkdown.markdown_to_block(markdown)

        html_nodes = []
        for block in blocks:
            block_type = BlockMarkdown.block_to_block_type(block)
            html_nodes.append(Helper.block_to_html_node(block_type, block))

        return ParentNode(tag="div", children=html_nodes)

    def block_to_html_node(block_type, block_value):
        if block_type == BlockMarkdown.block_type_heading:
            return Helper.block_to_heading_node(block_value)

        if block_type == BlockMarkdown.block_type_paragraph:
            return Helper.block_to_paragraph_node(block_value)

        if block_type == BlockMarkdown.block_type_code:
            return Helper.block_to_code_node(block_value)

        if block_type == BlockMarkdown.block_type_quote:
            return Helper.block_to_quote_node(block_value)

        if block_type == BlockMarkdown.block_type_unordered_list:
            return Helper.block_to_ulist_node(block_value)

        if block_type == BlockMarkdown.block_type_ordered_list:
            return Helper.block_to_olist_node(block_value)

        raise ValueError("Invalid Block: block type is not valid")

    def block_to_heading_node(block_value):
        if not block_value.startswith("#"):
            raise ValueError("Invalid Heading Block: not start with #")

        level = 0
        for c in block_value:
            if c == "#":
                level += 1
            else:
                break

        if level + 1 >= len(block_value):
            raise ValueError(f"Invalid Heading Block: level {level}")

        text = block_value[level + 1 :]
        html_nodes = Helper.text_to_children(text)
        return ParentNode(tag=f"h{level}", children=html_nodes)

    def block_to_paragraph_node(block_value):
        html_nodes = Helper.text_to_children(block_value)
        return ParentNode(tag="p", children=html_nodes)

    def block_to_code_node(block_value):
        if not block_value.startswith("```") or not block_value.endswith("```"):
            raise ValueError(
                "Invalid Code Block: not start with ``` or not end with ```"
            )

        text = block_value[4:-3]
        html_nodes = Helper.text_to_children(text)
        code_block = ParentNode(tag="code", children=html_nodes)
        return ParentNode(tag="pre", children=[code_block])

    def block_to_quote_node(block_value):
        lines = block_value.split("\n")

        new_lines = []
        for line in lines:
            if not line.startswith("> "):
                raise ValueError("Invalid Quote Block: not start with > ")

            new_lines.append(line.lstrip(">").strip())

        content = " ".join(new_lines)
        html_nodes = Helper.text_to_children(content)
        return ParentNode(tag="blockquote", children=html_nodes)

    def block_to_ulist_node(block_value):
        lines = block_value.split("\n")

        lis = []
        for line in lines:
            text = line[2:]
            inline_text = Helper.text_to_children(text)
            lis.append(ParentNode(tag="li", children=inline_text))

        return ParentNode(tag="ul", children=lis)

    def block_to_olist_node(block_value):
        lines = block_value.split("\n")

        lis = []
        for line in lines:
            text = line[3:]
            inline_text = Helper.text_to_children(text)
            lis.append(ParentNode(tag="li", children=inline_text))

        return ParentNode(tag="ol", children=lis)

    def text_to_children(text):
        textnodes = TextNode.text_to_textnodes(text)
        children = []

        for textnode in textnodes:
            children.append(TextNode.text_node_to_html_node(textnode))

        return children

    def block_to_parent_node(block_type):
        if block_type == BlockMarkdown.block_type_heading:
            return ParentNode(tag="h1", children=[], props=None)

        if block_type == BlockMarkdown.block_type_code:
            return ParentNode(tag="code", children=[], props=None)

        if block_type == BlockMarkdown.block_type_quote:
            return ParentNode(tag="blockquote", children=[], props=None)

        if block_type == BlockMarkdown.block_type_unordered_list:
            return ParentNode(tag="ul", children=[], props=None)

        if block_type == BlockMarkdown.block_type_ordered_list:
            return ParentNode(tag="ol", children=[], props=None)

        return ParentNode(tag="p", children=[], props=None)
