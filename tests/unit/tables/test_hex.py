import pytest
from src.tables.hex import Hex
from src.tables.constants import GroundUnitTypeAdditional, TerrainType


def test_effects_modifer():
    h = Hex()
    effects = h.effects_modifer(TerrainType.DESERT, GroundUnitTypeAdditional.MOTORISED)
    print(effects)
    assert 0 == effects['drm']
    assert 'Y' == effects['ASE']
    assert 1.50 == effects[GroundUnitTypeAdditional.MOTORISED][0]

