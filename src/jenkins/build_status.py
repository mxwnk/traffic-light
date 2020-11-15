from enum import Enum


class BuildStatus(Enum):
    OK = 1
    BUILDING = 2
    FAILED = 3
