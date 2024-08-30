import ruamel.yaml
import json

yaml = ruamel.yaml.YAML(typ="safe")

with open("example.json", "r") as f:
    data = json.load(f)

with open("example_out.yaml", "w") as f:
    yaml.dump(data, f)
