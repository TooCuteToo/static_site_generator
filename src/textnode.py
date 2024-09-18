class TextNode:
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
