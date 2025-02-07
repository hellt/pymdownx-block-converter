import unittest

import block_conv


class TestAdmonition(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # full diff output
        self.maxDiff = None

    def test_admonition_default(self):
        """Convert admonitions of the common/default syntax"""
        name = "admonition"
        path = f"tests/{name}"

        with open(f"{path}/{name}.md") as fh:
            text = fh.read()

        with open(f"{path}/{name}_expected.md") as fh:
            expected_text = fh.read()

        self.assertEqual(block_conv.update_admonition(text), expected_text)

    def test_admonition_no_spaces(self):
        """Convert admonitions with no spaces after exclamation marks"""
        name = "admonition_no_spaces"
        path = f"tests/{name}"

        with open(f"{path}/{name}.md") as fh:
            text = fh.read()

        with open(f"{path}/{name}_expected.md") as fh:
            expected_text = fh.read()

        self.assertEqual(block_conv.update_admonition(text), expected_text)

    def test_admonition_many_spaces(self):
        """Convert admonitions with no spaces after exclamation marks"""
        name = "admonition_many_spaces"
        path = f"tests/{name}"

        with open(f"{path}/{name}.md") as fh:
            text = fh.read()

        with open(f"{path}/{name}_expected.md") as fh:
            expected_text = fh.read()

        self.assertEqual(block_conv.update_admonition(text), expected_text)


if __name__ == "__main__":
    unittest.main()
