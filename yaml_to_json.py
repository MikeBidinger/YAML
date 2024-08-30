import ruamel.yaml
import json

yaml = ruamel.yaml.YAML(typ="safe")

with open("example.yaml", "r") as f:
    data = yaml.load(f)

with open("example_out.json", "w") as f:
    json.dump(data, f, indent=4)
