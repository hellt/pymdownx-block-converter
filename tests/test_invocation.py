import unittest
from unittest.mock import patch

import block_conv


class TestInvocation(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # full diff output
        self.maxDiff = None

        self.prog = "block_conv.py"
        self.path = "tests/invocation"
        self.file_list = [
            f"{self.path}/one.md",
            f"{self.path}/two.md",
            f"{self.path}/three.md",
        ]

    def test_arg_file(self):
        """Test the condition where a single file is the argument"""
        file = f"{self.path}/one.md"

        with patch("sys.argv", [self.prog, file]):
            target = block_conv.parse_args()
            self.assertEqual(target, file)

            md_files = block_conv.enumerate_markdown_files(target)
            self.assertEqual(len(md_files), 1) and self.assertIs(
                md_files, [file]
            )

    def test_arg_directory(self):
        """Test the condition where a directory is the argument"""
        with patch("sys.argv", [self.prog, self.path]):
            target = block_conv.parse_args()
            self.assertEqual(target, self.path)

            md_files = block_conv.enumerate_markdown_files(target)
            self.assertEqual(len(md_files), 3) and self.assertIs(
                md_files, self.file_list
            )

    def test_arg_missing(self):
        """Test the condition where an argument is not specified"""

        with patch("sys.argv", [self.prog]):
            target = block_conv.parse_args()
            self.assertIsNone(target)

            md_files = block_conv.enumerate_markdown_files(
                target, path=self.path
            )
            self.assertEqual(len(md_files), 3) and self.assertIs(
                md_files, self.file_list
            )


if __name__ == "__main__":
    unittest.main()
