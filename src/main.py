from helper import Helper


def main():
    str = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"

    children = Helper.markdown_to_html_node(str)
    print(children)


if __name__ == "__main__":
    main()
