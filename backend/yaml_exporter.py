# yaml_exporter.py

import yaml

def export_yaml(script_data, output_file):

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        yaml.dump(
            script_data,
            f,
            allow_unicode=True,
            sort_keys=False
        )
