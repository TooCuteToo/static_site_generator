from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None or len(self.tag) == 0:
            raise ValueError("Invalid ParentNode: no tag")

        if self.children is None:
            raise ValueError("Invalid ParentNode: no children")

        html_str = ""
        for child in self.children:
            html_str += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{html_str}</{self.tag}>"
