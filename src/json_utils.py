import json

from logger import get_logger

logger = get_logger(__name__)


def from_file(path):
    try:
        f = open(path, "r", encoding="utf-8")
        data = json.load(f)
        f.close()
        return data

    except Exception as ex:
        logger.error(ex)


def to_file(file_name, data):
    with open(file_name,  'w', encoding="utf-8") as json_file:
        json_file.write(data)

