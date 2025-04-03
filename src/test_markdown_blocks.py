import unittest
from markdown_blocks import markdown_to_blocks


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


if __name__ == "__manin__":
    unittest.main()
