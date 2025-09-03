from collections import Counter
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

        # yes, these test Markdown files are empty
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

            self.assertEqual(target[0], file)

            md_files = block_conv.gather_markdown_files(target)
            self.assertEqual(len(md_files), 1)
            self.assertEqual([str(m) for m in md_files], [file])

    def test_arg_directory(self):
        """Test the condition where a single directory is the argument"""
        with patch("sys.argv", [self.prog, self.path]):
            target = block_conv.parse_args()

            self.assertEqual(target[0], self.path)

            md_files = list(block_conv.gather_markdown_files(target))
            self.assertEqual(len(md_files), 3)
            for m in md_files:
                self.assertIn(str(m), self.file_list)

    def test_arg_missing(self):
        """Test the condition where an argument is not specified"""
        with patch("sys.argv", [self.prog]):
            target = block_conv.parse_args()
            self.assertEqual(target, [])

            md_files = list(
                block_conv.gather_markdown_files(
                    target, path=self.path
                )
            )

            self.assertEqual(len(md_files), 3)
            for m in md_files:
                self.assertIn(str(m), self.file_list)

    def test_arg_multiple_files(self):
        """Test the condition where multiple file arguments are specified"""
        files = [f"{self.path}/two.md", f"{self.path}/three.md"]

        with patch("sys.argv", [self.prog, *files]):
            target = block_conv.parse_args()

            md_files = list(block_conv.gather_markdown_files(target))
            self.assertEqual(len(md_files), 2)
            for m in md_files:
                self.assertIn(str(m), files)

    def test_arg_multiple_file_dir(self):
        """
        Test the condition where multiple file and dir arguments are
        specified. Also tests for the removal of duplicates.
        """
        files = [f"{self.path}/two.md", f"{self.path}"]

        with patch("sys.argv", [self.prog, *files]):
            target = block_conv.parse_args()

            # parse first target (single file)
            md_files = list(block_conv.gather_markdown_files(target))
            self.assertEqual(len(md_files), 3)
            for m in md_files:
                self.assertIn(str(m), self.file_list)



if __name__ == "__main__":
    unittest.main()
