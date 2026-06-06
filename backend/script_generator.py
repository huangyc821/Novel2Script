# script_generator.py

def generate_scenes(chapters, characters):

    scenes = []

    for idx, chapter in enumerate(chapters):

        scene = {
            "scene_id": idx + 1,
            "location": "未知地点",
            "time": "未知时间",
            "summary": chapter[:50],
            "dialogues": []
        }

        for character in characters[:2]:

            scene["dialogues"].append(
                {
                    "speaker": character,
                    "content": "这里是自动生成的对白。"
                }
            )

        scenes.append(scene)

    return scenes
