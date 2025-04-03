
def markdown_to_blocks(markdown):
    raw_blocks = markdown.strip().split("\n\n")
    blocks = [block.strip() for block in raw_blocks if block.strip()]
    return blocks


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
