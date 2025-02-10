import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="a", value="Click here")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_attributes(self):
        node = HTMLNode(tag="a", value="Click", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr_method(self):
        node = HTMLNode(tag="p", value="Hello World!", props={"class": "text-bold"})
        expected_repr = "HTMLNode(tag=p, value=Hello World!, children=[], props={'class': 'text-bold'})"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.mian()
