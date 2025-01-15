from dataclasses import dataclass
from typing import Self

from src.events.base import BaseEvent


@dataclass(slots=True, frozen=True)
class HarvestUsedEvent(BaseEvent):
    entity_id: int
    element_id: int
    skill_id: int
    duration: int
    can_move: bool

    @staticmethod
    def get_signature() -> bytes:
        return b"hzm"

    @classmethod
    def from_proto(cls, proto) -> Self:
        return cls(
            proto.entity_id,
            proto.element_id,
            proto.skill_id,
            proto.duration,
            proto.can_move,
       )
