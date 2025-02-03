import unittest

import block_conv


class TestTab(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # full diff output
        self.maxDiff = None

    def test_tab(self):
        """Convert tab blocks"""
        name = "tab"
        path = f"tests/{name}"

        with open(f"{path}/{name}.md") as fh:
            text = fh.read()

        with open(f"{path}/{name}_expected.md") as fh:
            expected_text = fh.read()

        self.assertEqual(block_conv.update_tabs(text), expected_text)


if __name__ == "__main__":
    unittest.main()
