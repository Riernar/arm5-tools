import pydantic

from pyarm5 import bases
from pyarm5.datamodels import arts


class VisAmount(bases.FrozenModel):
    """An amount of vis"""

    art: arts.HermeticArt | str  # support custom arts
    amount: int


class VisTransaction(bases.FrozenModel):
    """A vis source"""

    season: str  # support custom season
    year: int
    amounts: tuple[VisAmount, ...]

    description: str | None = None
    year_end: int | None = None
    owner: str | None = None
