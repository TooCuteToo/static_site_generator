class BlockMarkdown:

    block_type_heading = "heading"
    block_type_paragraph = "paragraph"
    block_type_code = "code"
    block_type_quote = "quote"
    block_type_unordered_list = "unordered_list"
    block_type_ordered_list = "ordered_list"

    def markdown_to_block(markdown):
        blocks = markdown.split("\n\n")
        filterd_blocks = []

        for item in blocks:
            if item == "":
                continue

            filterd_blocks.append(item.strip())

        return filterd_blocks

    def block_to_block_type(block):
        if BlockMarkdown.check_heading(block):
            return BlockMarkdown.block_type_heading

        lines = block.split("\n")

        if (
            lines[0].startswith("```")
            and lines[-1].startswith("```")
            and len(lines) > 1
        ):
            return BlockMarkdown.block_type_code

        is_quote_block = True
        is_ordered_list = True
        is_unordered_list = True

        for i in range(0, len(lines)):
            if not lines[i].startswith(">"):
                is_quote_block = False
            if not lines[i].startswith("* ") and not lines[i].startswith("- "):
                is_unordered_list = False
            if not lines[i].startswith(f"{i + 1}. "):
                is_ordered_list = False

        if is_quote_block:
            return BlockMarkdown.block_type_quote
        if is_ordered_list:
            return BlockMarkdown.block_type_ordered_list
        if is_unordered_list:
            return BlockMarkdown.block_type_unordered_list

        return BlockMarkdown.block_type_paragraph

    def check_heading(str):
        if not str.startswith("#"):
            return False

        count = 0
        for c in str:
            if c == "#":
                count += 1
            else:
                break

        if (
            (count >= 1 and count <= 6)
            and str[count] == " "
            and len(str) > count + 1
            and str[count + 1 :].strip()
        ):
            return True

        return False
