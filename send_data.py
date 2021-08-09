import json
from os import name
import requests
from rich import print
from pathlib import Path


def load_data(json_path: Path):
    return json.loads(json_path.read_text())


def main():

    json_path = Path("./sample_data.json")

    response = requests.post(
        f"http://127.0.0.1:8000/model/", json=json.loads(json_path.read_text())
    )

    print(response.json())


if __name__ == "__main__":
    main()
