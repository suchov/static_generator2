from enum import Enum


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
    lines = block.strip().split("\n")

    # Check for code block
    if lines[0].strip().startswith("```") and lines[-1].strip().endswith("```"):
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
