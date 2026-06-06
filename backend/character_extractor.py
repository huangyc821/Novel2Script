# character_extractor.py

import re
from collections import Counter

def extract_characters(text):

    names = re.findall(
        r'[\u4e00-\u9fa5]{2,3}',
        text
    )

    counter = Counter(names)

    characters = []

    for name, count in counter.most_common(10):

        if count >= 2:
            characters.append(name)

    return characters[:5]
