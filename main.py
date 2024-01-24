import json
from typing import Dict, Any
import cairo


def read_json_line(FILEPATH: str) -> [Dict[str, Any]]:
    """
    Reads a JSON file and returns a list of dictionaries with the coordinates
    """
    shape_coordinates = []
    file = open(FILEPATH, mode="r")
    # read a single lines from a
    for line in file.readline():
        # deserialize it to a dictionary
        cords = json.loads(line)
        shape_coordinates.append(cords)
    file.close()
    return shape_coordinates