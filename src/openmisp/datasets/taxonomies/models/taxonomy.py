from typing import Dict, Optional

from pydantic import BaseModel, Field


class Entry(BaseModel):
    uuid: str
    value: str
    namespace: str
    category: Optional[str] = None
    expanded: Optional[str] = None
    description: Optional[str] = None
    numerical_value: Optional[float] = None

    def __str__(self):
        return self.value

    @property
    def tag(self) -> str:
        if self.category:
            return f"{self.namespace}:{self.category}:{self.value}"
        return f"{self.namespace}:{self.value}"


class _Base(BaseModel):
    entries: Dict[str, Entry]

    def __getattr__(self, item: str) -> Entry:
        if item in self.entries:
            return self.entries[item]
        raise AttributeError(f"{item} not found")

    def __dir__(self):
        return list(self.entries.keys()) + super().__dir__()

    def __iter__(self):
        return iter(self.entries.values())

    def keys(self):
        return self.entries.keys()

    def values(self):
        return self.entries.values()

    def items(self):
        return self.entries.items()


class Category(_Base):
    name: str
    exclusive: Optional[bool] = False


class Taxonomy(_Base):
    namespace: str
    description: Optional[str] = ""
    uuid: str
    version: int
    categories: Optional[Dict[str, Category]] = Field(default_factory=dict)

    def __getattr__(self, item: str) -> Category | Entry:
        if item in self.categories:
            return self.categories[item]
        return super().__getattr__(item)

    def __dir__(self):
        return super().__dir__() + list(self.categories.keys())
