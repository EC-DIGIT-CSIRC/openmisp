"""Taxonomy model for COPINE Scale."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CopineScaleTaxonomyPredicate(str, Enum):
    LEVEL_10 = "level-10"
    LEVEL_9 = "level-9"
    LEVEL_8 = "level-8"
    LEVEL_7 = "level-7"
    LEVEL_6 = "level-6"
    LEVEL_5 = "level-5"
    LEVEL_4 = "level-4"
    LEVEL_3 = "level-3"
    LEVEL_2 = "level-2"
    LEVEL_1 = "level-1"


class CopineScaleTaxonomy(BaseModel):
    """Model for the COPINE Scale taxonomy."""

    namespace: str = "copine-scale"
    description: str = """The COPINE Scale is a rating system created in Ireland and used in the United Kingdom to categorise the severity of images of child sex abuse. The scale was developed by staff at the COPINE (Combating Paedophile Information Networks in Europe) project. The COPINE Project was founded in 1997, and is based in the Department of Applied Psychology, University College Cork, Ireland."""
    version: int = 3
    exclusive: bool = True
    predicates: List[CopineScaleTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
