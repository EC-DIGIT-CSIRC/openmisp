"""Taxonomy model for misinformation-website-label."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class MisinformationWebsiteLabelTaxonomyPredicate(str, Enum):
    FAKE_NEWS = "fake-news"
    SATIRE = "satire"
    EXTREME_BIAS = "extreme-bias"
    CONSPIRACY = "conspiracy"
    RUMOR = "rumor"
    STATE_NEWS = "state-news"
    JUNK_SCIENCES = "junk-sciences"
    HATE_NEWS = "hate-news"
    CLICKBAIT = "clickbait"
    PROCEED_WITH_CAUTION = "proceed-with-caution"
    POLITICAL = "political"
    CREDIBLE = "credible"
    UNKNOWN = "unknown"


class MisinformationWebsiteLabelTaxonomySatireEntry(str, Enum):
    HUMOR = "humor"
    IRONY = "irony"
    EXAGGERATION = "exaggeration"
    FALSE_INFORMATION = "false-information"


class MisinformationWebsiteLabelTaxonomyExtremeBiasEntry(str, Enum):
    PROPAGANDA = "propaganda"
    DECONTEXTUALIZED_INFORMATION = "decontextualized-information"
    OPINIONS_DISTORDED_AS_FACTS = "opinions-distorded-as-facts"


class MisinformationWebsiteLabelTaxonomyRumorEntry(str, Enum):
    RUMORS = "rumors"
    GOSSIP = "gossip"
    INNUENDO = "innuendo"
    UNVERIFIED_CLAIMS = "unverified-claims"


class MisinformationWebsiteLabelTaxonomyHateNewsEntry(str, Enum):
    RACISM = "racism"
    MISOGYNY = "misogyny"
    HOMOPHOBIA = "homophobia"
    DISCRIMINATION_OTHER = "discrimination-other"


class MisinformationWebsiteLabelTaxonomy(BaseModel):
    """Model for the misinformation-website-label taxonomy."""

    namespace: str = "misinformation-website-label"
    description: str = """classification for the identification of type of misinformation among websites. Source:False, Misleading, Clickbait-y, and/or Satirical News Sources by Melissa Zimdars 2019"""
    version: int = 1
    exclusive: bool = False
    predicates: List[MisinformationWebsiteLabelTaxonomyPredicate] = []
    satire_entries: List[MisinformationWebsiteLabelTaxonomySatireEntry] = []
    extreme_bias_entries: List[MisinformationWebsiteLabelTaxonomyExtremeBiasEntry] = []
    rumor_entries: List[MisinformationWebsiteLabelTaxonomyRumorEntry] = []
    hate_news_entries: List[MisinformationWebsiteLabelTaxonomyHateNewsEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
