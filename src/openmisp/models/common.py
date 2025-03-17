from enum import Enum


class Distribution(Enum):
    YOUR_ORGANIZATION_ONLY = 0
    THIS_COMMUNITY_ONLY = 1
    CONNECTED_COMMUNITIES = 2
    ALL_COMMUNITIES = 3
    SHARING_GROUP = 4
    INHERIT = 5


class Analysis(Enum):
    INITIAL = 0
    ONGOING = 1
    COMPLETED = 2


class ThreatLevel(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    UNDEFINED = 4
