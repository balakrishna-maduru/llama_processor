from enum import Enum

class DBConstants(Enum):
    mongo = "mongo"
    host = "host"
    port = "port"
    db = "db"
    collection = "collection"

class FileConstants(Enum):
    archive_dir = "archive_dir"
    input = "input"
