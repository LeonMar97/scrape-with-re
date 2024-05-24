import json


def save_to_json(file, data) -> bool:
    """tries saving file data to json"""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        # should be logged to somewhere instead..
        print(e)
        return False
