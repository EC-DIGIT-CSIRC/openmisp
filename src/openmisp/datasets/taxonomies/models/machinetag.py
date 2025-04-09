from typing import Optional

from pydantic import BaseModel, Field


class Predicate(BaseModel):
    uuid: str
    value: str
    expanded: Optional[str] = None
    exclusive: Optional[bool] = False


class Entry(BaseModel):
    uuid: str
    value: str
    expanded: Optional[str] = None


class Value(BaseModel):
    predicate: str
    entry: list[Entry]


class MachineTag(BaseModel):
    uuid: str
    namespace: str
    description: str
    version: int
    predicates: list[Predicate]
    values: Optional[list[Value]] = Field(default_factory=list)
