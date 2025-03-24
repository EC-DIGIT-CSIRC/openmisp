from enum import Enum

from pymisp import MISPTag


def create_tag(value: str):
    tag = MISPTag()
    tag.name = f'misp:confidence-level="{value}"'
    return tag


class Confidence(Enum):
    COMPLETELY_CONFIDENT = create_tag("completely-confident")
    USUALLY_CONFIDENT = create_tag("usually-confident")
    FAIRLY_CONFIDENT = create_tag("fairly-confident")
    RARELY_CONFIDENT = create_tag("rarely-confident")
    UNCONFIDENT = create_tag("unconfident")
    CANNOT_BE_EVALUATED = create_tag("confidence-cannot-be-evaluated")

    @staticmethod
    def get(value: int):
        if value < 0 or value > 100:
            raise ValueError("Value must be between 0 and 100")

        if value == 100:
            return Confidence.COMPLETELY_CONFIDENT
        elif value >= 75:
            return Confidence.USUALLY_CONFIDENT
        elif value >= 50:
            return Confidence.FAIRLY_CONFIDENT
        elif value >= 25:
            return Confidence.RARELY_CONFIDENT
        else:
            return Confidence.UNCONFIDENT
