#!/usr/bin/env python3
from pathlib import Path
import re
import sys

# huge thanks to tiangolo for the initial version of this script
# https://github.com/tiangolo/sqlmodel/pull/712
# https://github.com/tiangolo/sqlmodel/pull/713
# https://github.com/facelessuser/pymdown-extensions/discussions/1973#discussioncomment-7697040


def update_block(content, re_str):
    def replace(match: re.Match):
        type_ = match.group("type")
        title = match.group("title")
        block = match.group("content")
        deindented_block = re.sub(r"^ {4}", "", block, flags=re.MULTILINE)

        m = re.match(r"\?{3}(?P<open>\+)?", match.group())
        question_marks = True if m else False
        open_ = m.group("open") if m else None

        result = "/// details" if question_marks else f"/// {type_}"

        if title:
            result += f" | {title}"

        if question_marks:
            result += f"\n    type: {type_}"

        if open_:
            result += "\n    open: True"

        result += f"\n{deindented_block.strip()}\n"
        result += "///\n\n"
        return result

    new_content = re.sub(re_str, replace, content)

    return new_content.strip() + "\n"


def update_admonition(content):
    # https://regex101.com/r/8CWkrH/1
    re_str = (
        r"!!!\s*(?P<type>[^\n\s\"]*)\s*(\"(?P<title>[^\n\"]*)\")?\n"
        r"(?P<content>(\n|    .*)*)\n*"
    )

    return update_block(content, re_str)


def update_details_question_marks(content):
    re_str = (
        r"\?{3}\+?\s*(?P<type>[^\n\s\"]*)\s*(\"(?P<title>[^\n\"]*)\")?\n"
        r"(?P<content>(\n|    .*)*)\n*"
    )

    return update_block(content, re_str)


def update_details(content):
    re_str = r"<summary>((\n|.)*)</summary>"
    open_true_str = "    open: True\n"

    new_content = content

    all_starts = re.finditer(r"<details(\s+open.*)?>", content)
    all_ends = re.finditer("</details>", content)
    for start, end in zip(all_starts, all_ends):
        sub_content = content[start.start() : end.end()]

        m = re.search(re_str, sub_content)
        summary = f" | {m.group(1).strip()}" if m else ""

        sub_content_internal = content[start.end() : end.start()].strip()

        sub_content_no_summary = re.sub(
            re_str, "", sub_content_internal
        ).strip()

        new_sub_content = (
            f"/// details{summary}\n"
            f"{open_true_str if 'open' in start.group() else ''}"
            f"{sub_content_no_summary}\n///"
        )

        new_content = new_content.replace(sub_content, new_sub_content)

    return new_content


def update_tabs(content):
    # https://regex101.com/r/8CWkrH/1
    re_str = r"===\s?\"(?P<title>.+)\"\n(?P<content>(\n|    .*)*)\n*"

    def replace(match: re.Match):
        title = match.group("title")
        block = match.group("content")
        deindented_block = re.sub(r"^ {4}", "", block, flags=re.MULTILINE)
        result = "/// tab"
        if title:
            result += f" | {title}"
        result += f"\n{deindented_block.strip()}\n"
        result += "///\n\n"
        return result

    new_content = re.sub(re_str, replace, content)

    return new_content.strip() + "\n"


def parse_args():
    try:
        # return paths if one or more files have been specified as arguments
        return sys.argv[1:]
    # there's going to be an IndexError if no file/path argument was specified
    except IndexError:
        return [None]


def gather_markdown_files(targets, path="/docs"):
    md_files = []

    # if there was no argument in argv
    if not targets:
        # backward compatible with initial container configuration
        md_files += list(Path(path).glob("**/*.md"))
    else:
        for target in targets:
            if Path(target).is_file():
                md_files += [Path(target)]
            # must be a directory, right?
            else:
                md_files += list(Path(target).glob("**/*.md"))

    # remove duplicates by type casting to a set
    return set(md_files)


if __name__ == "__main__":
    targets = parse_args()

    md_files = gather_markdown_files(targets)

    for md_file in md_files:
        content = md_file.read_text()

        content = update_admonition(content)
        content = update_details(content)
        content = update_details_question_marks(content)
        content = update_tabs(content)

        md_file.write_text(content)
