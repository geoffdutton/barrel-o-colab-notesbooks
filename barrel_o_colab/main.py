import json
import os
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(os.path.join(__file__, "..")))


def txt_to_json(txt_file, json_file):
    with open(Path(ROOT_DIR) / txt_file, "r") as f:
        lines = f.read().splitlines()

    with open(Path(ROOT_DIR) / json_file, "w") as f:
        json.dump(lines, f, indent=4, sort_keys=True)


def main():
    print(f"ROOT_DIR: {ROOT_DIR}")
    txt_to_json("exts.txt", "exts.json")


if __name__ == "__main__":
    res = main()
    print(res)
