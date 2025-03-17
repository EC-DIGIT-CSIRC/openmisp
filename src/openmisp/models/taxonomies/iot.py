"""Taxonomy model for Internet of Things."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class IotTaxonomyPredicate(str, Enum):
    TCOM = "TCom"
    SSL = "SSL"
    DSL = "DSL"


class IotTaxonomyTcomEntry(str, Enum):
    T_0 = "0"
    T_1 = "1"
    T_2 = "2"
    T_3 = "3"
    T_4 = "4"
    T_5 = "5"
    T_6 = "6"
    T_7 = "7"


class IotTaxonomySslEntry(str, Enum):
    T_0 = "0"
    T_1 = "1"
    T_2 = "2"
    T_3 = "3"
    T_4 = "4"


class IotTaxonomyDslEntry(str, Enum):
    T_0 = "0"
    T_1 = "1"
    T_2 = "2"
    T_3 = "3"
    T_4 = "4"


class IotTaxonomy(BaseModel):
    """Model for the Internet of Things taxonomy."""

    namespace: str = "iot"
    description: str = """Internet of Things taxonomy, based on IOT UK report https://iotuk.org.uk/wp-content/uploads/2017/01/IOT-Taxonomy-Report.pdf"""
    version: int = 2
    exclusive: bool = False
    predicates: List[IotTaxonomyPredicate] = []
    tcom_entries: List[IotTaxonomyTcomEntry] = []
    ssl_entries: List[IotTaxonomySslEntry] = []
    dsl_entries: List[IotTaxonomyDslEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
