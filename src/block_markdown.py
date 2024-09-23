class BlockMarkdown:
    def markdown_to_block(markdown):
        blocks = markdown.split("\n\n")

        for i in range(0, len(blocks)):
            if blocks[i] == "":
                del blocks[i]
                continue

            blocks[i] = blocks[i].strip()

        return blocks
