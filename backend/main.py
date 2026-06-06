# main.py

from novel_parser import parse_novel
from character_extractor import extract_characters
from script_generator import generate_scenes
from yaml_exporter import export_yaml

INPUT_FILE = "../examples/sample_novel.txt"
OUTPUT_FILE = "../examples/sample_output.yaml"


def main():

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        novel_text = f.read()

    chapters = parse_novel(novel_text)

    characters = extract_characters(novel_text)

    scenes = generate_scenes(
        chapters,
        characters
    )

    script = {
        "title": "Novel2Script Output",
        "characters": characters,
        "scenes": scenes
    }

    export_yaml(
        script,
        OUTPUT_FILE
    )

    print("生成成功")
    print(f"章节数: {len(chapters)}")
    print(f"角色数: {len(characters)}")


if __name__ == "__main__":
    main()
