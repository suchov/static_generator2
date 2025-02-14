import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is a text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
                [
                    TextNode("This is a text with a ", TextType.TEXT),
                    TextNode("bolded", TextType.BOLD),
                    TextNode(" word", TextType.TEXT),
                ],
                new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
