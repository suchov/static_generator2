import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="a", value="Click here")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_attributes(self):
        node = HTMLNode(tag="a", value="Click", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr_method(self):
        node = HTMLNode(tag="p", value="Hello World!", props={"class": "text-bold"})
        expected_repr = "HTMLNode(tag=p, value=Hello World!, children=None, props={'class': 'text-bold'})"
        self.assertEqual(repr(node), expected_repr)

    def test_values(self):
        node = HTMLNode(
                "div",
                "I wish I could read",
        )
        self.assertEqual(
                node.tag,
                "div",
        )
        self.assertEqual(
                node.value,
                "I wish I could read",
        )
        self.assertEqual(
                node.children,
                None,
        )
        self.assertEqual(
                node.props,
                None,
        )


class TestLeafNode(unittest.TestCase):

    def test_leafnode_renders_plain_text(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leafnode_renders_with_tag(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

    def test_leafnode_renders_with_tag_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_teafnode_without_value_raise_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

if __name__ == "__main__":
    unittest.mian()
