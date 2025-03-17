"""Taxonomy model for Traffic Light Protocol."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class TlpTaxonomyPredicate(str, Enum):
    RED = "red"
    AMBER = "amber"
    AMBER_STRICT = "amber+strict"
    GREEN = "green"
    WHITE = "white"
    CLEAR = "clear"
    EX_CHR = "ex:chr"
    UNCLEAR = "unclear"


class TlpTaxonomy(BaseModel):
    """Model for the Traffic Light Protocol taxonomy."""

    namespace: str = "tlp"
    description: str = """The Traffic Light Protocol (TLP) (v2.0) was created to facilitate greater sharing of potentially sensitive information and more effective collaboration. Information sharing happens from an information source, towards one or more recipients. TLP is a set of four standard labels (a fifth label is included in amber to limit the diffusion) used to indicate the sharing boundaries to be applied by the recipients. Only labels listed in this standard are considered valid by FIRST. This taxonomy includes additional labels for backward compatibility which are no more validated by FIRST SIG."""
    version: int = 10
    exclusive: bool = True
    predicates: List[TlpTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
