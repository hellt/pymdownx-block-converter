import unittest

import block_conv


class TestTab(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # full diff output
        self.maxDiff = None

    def test_details_html_with_summary(self):
        """Convert HTML details blocks (with a summary)"""
        name = "details_html"
        path = f"tests/{name}"

        with open(f"{path}/{name}.md") as fh:
            text = fh.read()

        with open(f"{path}/{name}_expected.md") as fh:
            expected_text = fh.read()

        self.assertEqual(block_conv.update_details(text), expected_text)

    def test_details_html_expanded(self):
        """Convert HTML details blocks that are open/expanded"""
        name = "details_html_expanded"
        path = f"tests/{name}"

        with open(f"{path}/{name}.md") as fh:
            text = fh.read()

        with open(f"{path}/{name}_expected.md") as fh:
            expected_text = fh.read()

        self.assertEqual(block_conv.update_details(text), expected_text)

    def test_details_html_without_summary(self):
        """Convert HTML details blocks without a summary"""
        name = "details_no_summary"
        path = f"tests/{name}"

        with open(f"{path}/{name}.md") as fh:
            text = fh.read()

        with open(f"{path}/{name}_expected.md") as fh:
            expected_text = fh.read()

        self.assertEqual(block_conv.update_details(text), expected_text)

    def test_details_question_marks(self):
        """Convert details with question marks instead of HTML tags"""
        name = "details_question_marks"
        path = f"tests/{name}"

        with open(f"{path}/{name}.md") as fh:
            text = fh.read()

        with open(f"{path}/{name}_expected.md") as fh:
            expected_text = fh.read()

        self.assertEqual(
            block_conv.update_details_question_marks(text), expected_text
        )

    def test_details_question_marks_expanded(self):
        """Convert details with question marks that are open/expanded"""
        name = "details_question_marks_expanded"
        path = f"tests/{name}"

        with open(f"{path}/{name}.md") as fh:
            text = fh.read()

        with open(f"{path}/{name}_expected.md") as fh:
            expected_text = fh.read()

        self.assertEqual(
            block_conv.update_details_question_marks(text), expected_text
        )


if __name__ == "__main__":
    unittest.main()
