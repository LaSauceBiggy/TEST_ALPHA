from dataclasses import dataclass
from typing import Self

from src.events.base import BaseEvent


@dataclass(slots=True, frozen=True)
class HarvestCompletedEvent(BaseEvent):
    element_id: int
    skill_id: int

    @staticmethod
    def get_signature() -> bytes:
        return b"hyv"

    @classmethod
    def from_proto(cls, proto) -> Self:
        return cls(proto.element_id, proto.skill_id)
