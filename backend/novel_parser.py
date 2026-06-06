# novel_parser.py

import re

def parse_novel(text):
    """
    按 '第一章'、'第二章' 等划分章节
    """

    chapters = re.split(r'第[一二三四五六七八九十百\d]+章', text)

    chapters = [
        chapter.strip()
        for chapter in chapters
        if chapter.strip()
    ]

    return chapters
