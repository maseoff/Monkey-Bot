from dataclasses import dataclass


@dataclass(frozen=True)
class TConfig(object):
    TOKEN: str
    PARSE_MODE: str
    TEMP_FOLDER: str
    IMAGE_FODLER: str
