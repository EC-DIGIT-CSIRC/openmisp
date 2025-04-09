import json
from typing import Optional

from .models import Category, Entry, MachineTag, Taxonomy

FILENAME = "machinetag.json"


def normalize_key(key: str) -> str:
    return key.replace("-", "_").replace(":", "_").upper()


class Loader:
    def __init__(self, base_path: str):
        self._taxonomies = {}
        self._load(base_path)

    def _load(self, base_path: str):
        for path in base_path.iterdir():
            file = path / FILENAME

            if not file.is_file():
                continue

            with open(file, "r") as fp:
                data = json.load(fp)
                data = MachineTag(**data)

            taxonomy = self._load_taxonomy(data)
            codename = normalize_key(taxonomy.namespace)
            self._taxonomies[codename] = taxonomy

    def _load_taxonomy(self, data: dict) -> Taxonomy:
        categories = self._load_categories(data)

        entries = self._load_entries(
            data,
            namespace=data.namespace,
            lookup="predicates",
        )

        return Taxonomy(
            namespace=data.namespace,
            description=data.description,
            uuid=data.uuid,
            version=data.version,
            categories=categories,
            entries=entries,
        )

    def _load_categories(self, data: dict) -> dict[str, Category]:
        categories = {}

        for item in data.values:
            entries = self._load_entries(
                item,
                namespace=data.namespace,
                category=item.predicate,
                lookup="entry",
            )

            for predicate in data.predicates:
                if predicate.value != item.predicate:
                    continue

                codename = normalize_key(item.predicate)

                categories[codename] = Category(
                    name=predicate.value,
                    exclusive=predicate.exclusive,
                    entries=entries,
                )

        return categories

    def _load_entries(
        self,
        data: dict,
        namespace: str,
        category: Optional[str] = None,
        lookup: str = "entry",
    ) -> dict[str, Entry]:
        return {
            normalize_key(item.value): Entry(
                namespace=namespace,
                category=category,
                **item.dict(),
            )
            for item in getattr(data, lookup, [])
        }

    def __getattr__(self, item: str) -> Taxonomy:
        if item in self._taxonomies:
            return self._taxonomies[item]
        raise AttributeError(f"No taxonomy named '{item}'")

    def __dir__(self):
        return list(self._taxonomies.keys()) + super().__dir__()
