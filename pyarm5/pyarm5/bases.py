import enum
from typing import Any, Self

import pydantic


class StrFlag(enum.Flag):
    """Base class supporting converting str values to enum"""

    @classmethod
    def _missing_(cls: type[Self], value: Any) -> Self:
        if isinstance(value, str):
            value = value.lower()
            matches = {member for member in cls if member.name.lower().startswith(value)}
            match len(matches):
                case 0:
                    raise ValueError(
                        f"Invalid {cls.__name__} '{value}': expected one of {set(cls)}"
                    )
                case 1:
                    return matches.pop()
                case _:
                    raise ValueError(f"Ambiguous {cls.__name__} '{value}': matches {matches}")
        return super()._missing_(value)


class FrozenModel(pydantic.BaseModel, extra="forbid", frozen=True):
    """Pydantic BaseModel that is frozen and doesn't support extras"""
