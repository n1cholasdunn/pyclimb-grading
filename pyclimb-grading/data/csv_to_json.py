import csv
import json
from pydantic import BaseModel
from typing import Type
import os


class Boulder(BaseModel):
    score: int
    font: str
    v: str


class Route(BaseModel):
    score: int
    brazilian: str
    ewbank: str
    french: str
    norwegian: str
    saxon: str
    uiaa: str
    yds: str


class Ice(BaseModel):
    score: int
    ai: str
    wi: str


class Aid(BaseModel):
    score: int
    aid: str


def get_data(file_path: str, json_path: str, model: Type[BaseModel]):
    data = []

    try:
        with open(file_path, newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                row["score"] = int(row["score"])
                data.append(model(**row))
    except Exception as e:
        print(f"Error reading CSV file {file_path}: {e}")
        return []

    try:
        with open(json_path, "w") as json_file:
            json.dump([d.dict() for d in data], json_file)
    except Exception as e:
        print(f"Error writing JSON file {json_path}: {e}")
        return []

    return data


data_dir = os.path.join(os.getcwd(), "data")

CSV_PATH_BOULDER = os.path.join(data_dir, "boulder.csv")
JSON_PATH_BOULDER = os.path.join(data_dir, "boulder.json")
BOULDER_GRADE_TABLE = get_data(CSV_PATH_BOULDER, JSON_PATH_BOULDER, Boulder)

CSV_PATH_ROUTES = os.path.join(data_dir, "routes.csv")
JSON_PATH_ROUTES = os.path.join(data_dir, "routes.json")
ROUTES_GRADE_TABLE = get_data(CSV_PATH_ROUTES, JSON_PATH_ROUTES, Route)

CSV_PATH_ICE = os.path.join(data_dir, "ice.csv")
JSON_PATH_ICE = os.path.join(data_dir, "ice.json")
ICE_GRADE_TABLE = get_data(CSV_PATH_ICE, JSON_PATH_ICE, Ice)

CSV_PATH_AID = os.path.join(data_dir, "aid.csv")
JSON_PATH_AID = os.path.join(data_dir, "aid.json")
AID_GRADE_TABLE = get_data(CSV_PATH_AID, JSON_PATH_AID, Aid)
