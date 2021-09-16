from typing import List, TextIO


f: TextIO
lines: List[str]
read:  List[str]
cnt_read: int


if __name__ == "__main__":

    with open("./listbooks.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    read = [x for x in lines if x.startswith("* [x]")]

    cnt_read = len(read)

    lines[
        lines.index("<!-- Automated -->\n") + 2
    ] = f": `{cnt_read}/1000`\n"

    with open("./listbooks.md", "w", encoding="utf-8") as f:
        f.writelines(lines)
