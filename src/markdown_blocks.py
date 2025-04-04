from enum import Enum

from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import LeafNode, ParentNode


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    UNORDERED_LIST = "unordered_list"
    OLIST = "ordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    raw_blocks = markdown.strip().split("\n\n")
    blocks = [block.strip() for block in raw_blocks if block.strip()]
    return blocks


def block_to_block_type(block):
    lines = [line.strip() for line in block.strip().split("\n") if line.strip()]

    # Check for code block
    # Check for code block (MUST be triple backticks on a line alone)
    if lines[0].strip() == "```" and lines[-1].strip() == "```":
        return BlockType.CODE

    # Check for heading (1-6 # characters followed by space)
    if lines[0].startswith("#"):
        hashes, _, rest = lines[0].partition(" ")
        if 1 <= len(hashes) <= 6 and rest:
            return BlockType.HEADING

    # Check for quote block
    if all(line.strip().startswith(">") for line in lines):
        return BlockType.QUOTE

    # Check for unordered list
    if all(line.strip().startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Check for ordered list
    def is_ordered_list(lines):
        expected_number = 1
        for line in lines:
            line = line.strip()
            if not line.startswith(f"{expected_number}. "):
                return False
            expected_number += 1
        return True

    if is_ordered_list(lines):
        return BlockType.ORDERED_LIST

    # Default to paragraph
    return BlockType.PARAGRAPH


# TODO review this and try to understand
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = [block_to_html_node(block) for block in blocks]
    return ParentNode("div", children)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    lines = block.strip().split("\n")

    if block_type == BlockType.PARAGRAPH:
        cleaned = " ".join(line.strip() for line in block.splitlines())
        return ParentNode("p", text_to_children(cleaned))

    elif block_type == BlockType.HEADING:
        level = block.count("#", 0, block.find(" "))
        content = block[level+1:].strip()
        return ParentNode(f"h{level}", text_to_children(content))

    elif block_type == BlockType.CODE:
        lines = block.strip().split("\n")
        code_content = "\n".join(lines[1:-1]) + "\n"
        code_node = LeafNode("code", code_content)
        return ParentNode("pre", [code_node])

    elif block_type == BlockType.QUOTE:
        stripped = "\n".join([line.lstrip("> ").strip() for line in block.splitlines()])
        return ParentNode("blockquote", text_to_children(stripped))

    elif block_type == BlockType.UNORDERED_LIST:
        items = [line.lstrip("- ").strip() for line in block.splitlines()]
        return ParentNode("ul", [ParentNode("li", text_to_children(item)) for item in items])

    elif block_type == BlockType.ORDERED_LIST:
        items = [line[line.find(". ")+2:].strip() for line in block.splitlines()]
        return ParentNode("ol", [ParentNode("li", text_to_children(item)) for item in items])

    raise ValueError(f"Unsupported block type: {block_type}")


def text_to_children(text):
    return [text_node_to_html_node(node) for node in text_to_textnodes(text)]


"""
    def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
    """
