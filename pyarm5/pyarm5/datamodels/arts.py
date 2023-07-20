import enum
from typing import TypeAlias

from pyarm5 import bases


class HermeticTechnique(bases.StrFlag):
    """Enum of hermetic techniques. May be combined"""

    CREO = enum.auto()
    INTELLEGO = enum.auto()
    MUTO = enum.auto()
    PERDO = enum.auto()
    REGO = enum.auto()


class HermeticForm(bases.StrFlag):
    """Enum of hermetic forms. May be combined"""

    ANIMAL = enum.auto()
    AQUAM = enum.auto()
    AURAM = enum.auto()
    CORPUS = enum.auto()
    HERBAM = enum.auto()
    IGNEM = enum.auto()
    IMAGINEM = enum.auto()
    MENTEM = enum.auto()
    TERRAM = enum.auto()
    VIM = enum.auto()


HermeticArt: TypeAlias = HermeticTechnique | HermeticForm
