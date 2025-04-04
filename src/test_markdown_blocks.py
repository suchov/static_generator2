import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):

    def test_basic_blocks(self):
        md = """
# Heading

This is a paragraph with **bold** and _italic_.

- List item 1
- List item 2
"""
        expected = [
                "# Heading",
                "This is a paragraph with **bold** and _italic_.",
                "- List item 1\n- List item 2",
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_empty_lines_and_whitespaces(self):
        md = """


This is block one


This is block two

"""
        expected = [
                "This is block one",
                "This is block two",
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_paragraph_within_block(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `conde` here
This is the same paragraph on a new line

- This is a list
- with items
            """
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `conde` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>")


if __name__ == "__manin__":
    unittest.main()
