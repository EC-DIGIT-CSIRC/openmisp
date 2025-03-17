import re
from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict
from pymisp import MISPAttribute, MISPEvent, MISPObjectAttribute, MISPTag, PyMISP

from openmisp.validators import validate_client, validate_entity_type


class TagCriteria(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    pattern: Optional[str] = None

    @property
    def pattern_regex(self) -> Optional[str]:
        if self.pattern:
            return self.pattern.replace("%", ".*")
        return None


class TagService:
    def __init__(self, client: PyMISP):
        validate_client(client)
        self._client = client

    def create(self, *, name: str) -> MISPTag:
        tag = MISPTag()
        tag.name = name
        return tag

    def edit(self, tag: MISPTag, *, name: str) -> bool:
        validate_entity_type(tag, MISPTag)
        tag.name = name
        return True

    def get(
        self, entity: Union[MISPEvent, MISPObjectAttribute, MISPAttribute], criteria: TagCriteria
    ) -> Optional[MISPTag]:
        validate_entity_type(entity, (MISPEvent, MISPObjectAttribute, MISPAttribute))
        return next((tag for tag in self.list(entity, criteria)), None)

    def exists(self, entity: Union[MISPEvent, MISPObjectAttribute, MISPAttribute], criteria: TagCriteria) -> bool:
        validate_entity_type(entity, (MISPEvent, MISPObjectAttribute, MISPAttribute))
        return self.get(entity, criteria) is not None

    def list(
        self, entity: Union[MISPEvent, MISPObjectAttribute, MISPAttribute], criteria: TagCriteria
    ) -> List[MISPTag]:
        validate_entity_type(entity, (MISPEvent, MISPObjectAttribute, MISPAttribute))

        if criteria.pattern is None:
            return entity.tags

        return [tag for tag in entity.tags if re.match(criteria.pattern_regex, tag.name)]

    def _parent_link(self, entity: Union[MISPEvent, MISPObjectAttribute, MISPAttribute], tag: MISPTag) -> bool:
        validate_entity_type(tag, MISPTag)
        validate_entity_type(entity, (MISPEvent, MISPObjectAttribute, MISPAttribute))

        self._parent_unlink(entity, tag)

        entity.add_tag(tag)
        entity.edited = True
        return True

    def _parent_unlink(self, entity: Union[MISPEvent, MISPObjectAttribute, MISPAttribute], tag: MISPTag) -> bool:
        validate_entity_type(tag, MISPTag)
        validate_entity_type(entity, (MISPEvent, MISPObjectAttribute, MISPAttribute))

        for index, _tag in enumerate(entity.tags):
            if _tag.name == tag.name:
                entity.tags.pop(index)
                entity.edited = True
                return True

        return False

    def _parent_sync(
        self,
        current: Union[MISPEvent, MISPObjectAttribute, MISPAttribute],
        new: Union[MISPEvent, MISPObjectAttribute, MISPAttribute],
    ) -> bool:
        if not isinstance(current, type(new)):
            raise ValueError(f"Cannot sync {type(current).__name__} with {type(new).__name__}.")

        validate_entity_type(current, (MISPEvent, MISPObjectAttribute, MISPAttribute))
        validate_entity_type(new, (MISPEvent, MISPObjectAttribute, MISPAttribute))

        for current_tag in current.tags:
            for tag in new.tags:
                if current_tag.name == tag.name:
                    break
            else:
                self._client.untag(current.uuid, current_tag)

    def _list(self, criteria: TagCriteria) -> List[MISPTag]:
        if isinstance(criteria, TagCriteria):
            tags = self._client.search_tags(tagname=criteria.pattern, strict_tagname=True, pythonify=True)
            return [tag for tag in tags if not tag.name.startswith("misp-galaxy:")]
        else:
            raise ValueError("Invalid filter type.")
