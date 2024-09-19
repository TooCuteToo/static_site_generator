from htmlnode import *


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None or len(self.tag) == 0:
            raise ValueError("parent node must have a tag")

        if self.children is None or len(self.children) == 0:
            raise ValueError("parent node must have children")

        html_str = f"<{self.tag}>"
        for child in self.children:
            html_str += child.to_html()

        return html_str + f"</{self.tag}>"
