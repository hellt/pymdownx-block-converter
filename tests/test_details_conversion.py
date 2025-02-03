import unittest

import block_conv


class TestTab(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # full diff output
        self.maxDiff = None

    def test_details_with_summary(self):
        """Convert details blocks (with a summary)"""
        name = "details"
        path = f"tests/{name}"

        with open(f"{path}/{name}.md") as fh:
            text = fh.read()

        with open(f"{path}/{name}_expected.md") as fh:
            expected_text = fh.read()

        self.assertEqual(block_conv.update_details(text), expected_text)

    def test_details_without_summary(self):
        """Convert details blocks without a summary"""
        name = "details_no_summary"
        path = f"tests/{name}"

        with open(f"{path}/{name}.md") as fh:
            text = fh.read()

        with open(f"{path}/{name}_expected.md") as fh:
            expected_text = fh.read()

        self.assertEqual(block_conv.update_details(text), expected_text)


if __name__ == "__main__":
    unittest.main()
