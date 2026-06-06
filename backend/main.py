import yaml

script = {
    "title": "校园风云",

    "characters": [
        "张三",
        "李四"
    ],

    "scenes": [
        {
            "scene_id": 1,
            "location": "教室",
            "time": "上午",

            "summary": "张三来到教室上课。",

            "dialogues": [
                {
                    "speaker": "张三",
                    "content": "大家好。"
                },
                {
                    "speaker": "李四",
                    "content": "比赛准备得怎么样？"
                }
            ]
        }
    ]
}

with open(
    "../examples/sample_output.yaml",
    "w",
    encoding="utf-8"
) as f:
    yaml.dump(
        script,
        f,
        allow_unicode=True,
        sort_keys=False
    )

print("剧本生成成功")
