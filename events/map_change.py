from abc import abstractmethod
from dataclasses import dataclass
from typing import Self

from src.events.base import BaseEvent


@dataclass(slots=True, frozen=True)
class Skill:
    skill_id: int
    skill_instance_uid: int
    name_id: int

@dataclass(slots=True, frozen=True)
class Harverstable:
    cell_id: int
    element_id: int
    skill_enable: list[Skill]
    skill_disable: list[Skill]
    element_type_id: int
    is_present: bool


@dataclass(slots=True, frozen=True)
class MapChangeEvent(BaseEvent):
    map_id: int
    harverstables: list[Harverstable]

    @staticmethod
    def get_signature() -> bytes:
        return b"igr"

    @classmethod
    def from_proto(cls, proto) -> Self:
        cell_map = {
            e.element_id: (e.cell_id, not bool(e.state)) for e in proto.stated_elements
        }

        _h = []
        for i in proto.interactive_elements:
            _h.append(
                Harverstable(
                    cell_id=cell_map.get(i.element_id, (-1, False))[0],
                    is_present=cell_map.get(i.element_id, (-1, False))[1],
                    skill_enable=[Skill(
                    skill_id=x.skill_id,
                    skill_instance_uid=x.skill_instance_uid,
                    name_id=x.name_id,
                )  for x in i.enabled_skills],
                    skill_disable=[Skill(
                        skill_id=x.skill_id,
                        skill_instance_uid=x.skill_instance_uid,
                        name_id=x.name_id,
                    ) for x in i.disabled_skills],
                    element_id=i.element_id,
                    element_type_id=i.element_type_id,
                )
            )
        return cls(map_id=proto.map_id, harverstables=_h)
