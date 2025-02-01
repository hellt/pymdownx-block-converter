import re
from pathlib import Path

# huge thanks to tiangolo for this script
# https://github.com/tiangolo/sqlmodel/pull/712
# https://github.com/tiangolo/sqlmodel/pull/713
# https://github.com/facelessuser/pymdown-extensions/discussions/1973#discussioncomment-7697040


def update_admonition():
    md_files = list(Path("/docs").glob("**/*.md"))
    # https://regex101.com/r/8CWkrH/1
    re_str = r"!!!\s?(?P<type>[^\n\"]*)\s?(\"(?P<title>[^\n\"]*)\")?\n(?P<content>(\n|    .*)*)\n*"
    for md_file in md_files:
        content = md_file.read_text()

        def replace(match: re.Match):
            type_ = match.group("type")
            title = match.group("title")
            block = match.group("content")
            deindented_block = re.sub(r"^ {4}", "", block, flags=re.MULTILINE)
            result = f"/// {type_}"
            if title:
                result += f" | {title}"
            result += f"\n{deindented_block.strip()}\n"
            result += "///\n\n"
            return result

        new_content = re.sub(re_str, replace, content)
        md_file.write_text(new_content)


def update_details():
    md_files = list(Path("/docs").glob("**/*.md"))
    re_str = r"<summary>((\n|.)*)</summary>"
    for md_file in md_files:
        content = md_file.read_text()
        new_content = content
        all_starts = re.finditer("<details>", content)
        all_ends = re.finditer("</details>", content)
        for start, end in zip(all_starts, all_ends):
            sub_content = content[start.start() : end.end()]
            m = re.search(re_str, sub_content)
            assert m
            summary = m.group(1).strip()
            sub_content_internal = content[start.end() : end.start()].strip()
            sub_content_no_summary = re.sub(re_str, "", sub_content_internal).strip()
            new_sub_content = (
                f"/// details | {summary}\n\n{sub_content_no_summary}\n\n///"
            )
            new_content = new_content.replace(sub_content, new_sub_content)

        md_file.write_text(new_content)


def update_tabs():
    md_files = list(Path("/docs").glob("**/*.md"))
    # https://regex101.com/r/8CWkrH/1
    re_str = r"===\s?\"(?P<title>.+)\"\n(?P<content>(\n|    .*)*)\n*"
    for md_file in md_files:
        content = md_file.read_text()

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
        md_file.write_text(new_content)


if __name__ == "__main__":
    update_admonition()
    update_details()
    update_tabs()
